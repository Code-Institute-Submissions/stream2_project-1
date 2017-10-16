from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField("Name", [validators.required("Please enter your name")])
    email = StringField("Email", validators=[DataRequired("Please enter a valid email address"),
                                             validators.Email("Please enter a valid email address")])
    subject = StringField("Subject", validators=[DataRequired("Please enter the subject of your contact")])
    message = TextAreaField("Message", validators=[DataRequired("Please enter your message")])
    submit = SubmitField("Send")