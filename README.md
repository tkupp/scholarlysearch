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

Reference the included requirements.txt for a current list.

## Environments setup.

Please reference the included sample .env file provided in  the following location,
`scholarlysearch\example.env`  Instructions for setup are included in that file.

## Running
To start the application do the following:

`python manage.py runserver`

This will start the application in development mode under port 8000

To access the running copy go to 
`http://localhost:8000`

If you need to run this on another port, just reference the port as follows:

`python manage.py runserver 8010`

To run in production you will need to use a WSGI enabled webserver like  Gunicorn, uWSGI or Apache with the mod_wsgi module installed. Installation of these applications is outside of the scope of this document.

## Usage

It should be noted that this product is in the pre-Alpha stage, and as such most extended functionality is limited. 

You can utilize the UI from the search tab for limited results. Enter a search string in the field and press the `run` button to see a subset of the results. For Elsevier the results are limited to 25 results, starting with the first result. For Arxiv, the results are limited to 25 results, starting with the first result.

This application is better suited to be consumed via the provided REST API endpoints. From the main page click on the documentation tab to pull up a swagger page in a new tab. 

For searching against the Elsevier data, this link from Elseiver provides tips on searching.
https://dev.elsevier.com/sc_search_tips.html

For searching against Arxiv data, Arvix utilizes boolean `AND, OR, ANDNOT` searching logic. More detail is available on teh Arxiv site at,
https://info.arxiv.org/help/api/user-manual.html#detailed_examples
 

## Testing

There are some unit tests enabled to test functionality. 
To test type `python manage.py test` at the top level to run all tests.

Reference the Django documentation for more details on testing. https://docs.djangoproject.com/en/5.0/topics/testing/overview/

## How to report a bug or request a feature

First check the list of currently open [Issues](https://github.com/tkupp/scholarlysearch/issues) to make sure the bug or feature has not already been captured. If not, please submit a new issue!
 
## How to contribute

If you are interested in contributing to the project, please filter the open [Issues](https://github.com/tkupp/scholarlysearch/issues) by “good first issue” and/or “help wanted” to get started.

## API Documentation

This is provided on the swagger page. Reference the link on the documentation tab on the main UI page. As a general rule it is located under 

`http://localhost:8000/search/api/schema/swagger-ui/`

Your base url may vary based on your installation.

