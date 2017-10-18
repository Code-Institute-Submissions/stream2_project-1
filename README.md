# Stream 2 Project

## Overview

### What is this site for?
This site is a site for a fictional candidate running for the office of Governor of California.
It is primarily focused on displaying the use of a data-driven website.  
### What does it do?
It gives general information about the candidate and allows users to contact them to various 
means including a contact form. It also displays data from a school donations database taken from
[DonarsChoose.org](https://www.donorschoose.org/) using various visualisations and charts.

### How does it work?
The site is built with the Python microframework Flask. It uses MongoDB to store data and D3.js, DC.js
and Crossfilter.js to display and filter the data. The main layout of the site is built with HTML5, CSS
and Javascript.
### Testing

The site has been tested in Chrome, Firefox and Safari. Chrome device mode was used to check it for mobile
responsiveness.

## Features

### Existing Features
- Contact form
- Interactive data display

## Bugs

### Existing Bugs
- The data charts are not responsive to smaller screen sizes. I tried to find a way to do this but was unable 
get it to work at this time. I added a scroll bar so that the user can scroll across to see the hidden part of
the charts on smaller screens.
- In general I am not happy with the design for mobile devices. It is not as user friendly at smaller screen sizes
as I would like. However due to to time constraints I am unable to rectify it at this time.

## Tech Used

### Some of the tech used includes:
- [Flask](http://flask.pocoo.org/)
- [dc.js](https://dc-js.github.io/dc.js/)
- [D3.js](https://d3js.org/)
- [Crossfilter](https://square.github.io/crossfilter/)
- [keen-dashboards](https://keen.github.io/dashboards/)
- [intro.js](http://introjs.com/)
- [bootstrap](https://getbootstrap.com/)
- [jquery](https://jquery.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
- [queue.js](https://github.com/d3/d3-queue)


### Getting the code up and running
1. Firstly you will need to clone this repository by running the `git clone <project's Github URL>` command
2. Setup a virtual environment for the project
3. After you've that done you'll need to install the dependencies listed in the requirements.txt file.
4. You will need to create a secret key and enter your own mail settings in stream2_project.py.
5. Download the database from [DonarsChoose.org](https://www.donorschoose.org/)
6. You will need MongoDB installed locally to serve the data
7. Start an instance of MongoDB in a separate terminal window by running `mongod`

My site can be viewed on Heroku [here]( https://coylec-streamtwo-project.herokuapp.com/).