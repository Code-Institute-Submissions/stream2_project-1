from flask import Flask, render_template, request, flash
from pymongo import MongoClient
import json
import os
from forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__)

# app.secret_key = 'SECRET_KEY'

'''
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorsUSA'
COLLECTION_NAME = 'projects'
'''

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = ''
# app.config["MAIL_PASSWORD"] = ''
app.config["MAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')

mail.init_app(app)

app.secret_key = os.getenv('SECRET_KEY')
MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
DBS_NAME = os.getenv('MONGO_DB_NAME', 'donorsUSA')
COLLECTION_NAME = 'projects'
app.config['DEBUG'] = os.getenv('DEBUG', 'True')


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    A Flask view to serve the main home page.
    """
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Allfields are required')
            return render_template('home.html', form=form)
        else:
            msg = Message(form.subject.data, sender='coylec.devwork@gmail.com', recipients=['conradcoyle@gmail.com'])
            msg.body = """
                  From: %s <%s>
                  %s
                  """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('home.html', success=True)

    elif request.method == 'GET':
        return render_template("home.html", form=form)


@app.route('/statistics')
def stats():
    return render_template('statistics.html')


@app.route("/donorsUS/projects")
def donor_projects():
    """
    A Flask view to serve the project data from
    MongoDB in JSON format.
    """

    # A constant that defines the record fields that we wish to retrieve.
    FIELDS = {
        '_id': False, 'funding_status': True, 'school_state': True,
        'resource_type': True, 'poverty_level': True,
        'date_posted': True, 'total_donations': True
    }

    # Open a connection to MongoDB using a with statement such that the
    # connection will be closed as soon as we exit the with statement
    # The MONGO_URI connection is required when hosted using a remote mongo db.
    with MongoClient(MONGO_URI) as conn:
        # Define which collection we wish to access
        collection = conn[DBS_NAME][COLLECTION_NAME]
        # Retrieve a result set only with the fields defined in FIELDS
        # and limit the the results to 55000
        projects = collection.find(projection=FIELDS, limit=20000)
        # Convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(projects))


if __name__ == '__main__':
    app.run()
