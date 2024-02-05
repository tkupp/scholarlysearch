# Scholarly Search

## A project for CAS 502: Computation

Collaborators: Bill Terry & Travis Kupp

## Description
Searching and collecting data across multiple scholarly resources can be a daunting, tedious, and challenging task. This is especially true if large amounts of data are to be searched in a programmatic way. The goal is to provide a flexible and extensible tool to automate and simplify the task of searching across scholarly research.

## Installation

###
You need to provide a .env file underneath the scholarlysearch directory. This file is used to store sensitive information. 
Copy and modify the `scholarlysearch\example.env` file as needed. 

 This code has been developed with Python 3.11, it may work on version 3.9+

The following python libraries are required as a minimum. More may be required depending on your existing python environment. Use standard pip or pip3 to install.

<ul>
<li>django</li>
<li>django-bootstrap-v5</li>
<li>simplejson</li>
</ul>

## Running
To start the application do the following:

`python manage.py runserver`

This will start the application in development mode under port 8000

To access the running copy go to 
`http://localhost:8000`

If you need to run this on another port, just reference the port as follows:

`python manage.py runserver 8010`

To run in production you will need to use a WSGI enabled webserver like  Gunicorn, uWSGI or Apache with the mod_wsgi module installed. Installation of these applications is outside of the scope of this document.

## Testing

There are some unit tests enabled to test functionality. 
To test type `python manage.py test` at the top level to run all tests.

Reference the Django documentation for more details on testing. https://docs.djangoproject.com/en/5.0/topics/testing/overview/