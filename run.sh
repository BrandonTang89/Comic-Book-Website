#!/bin/bash

#Use for Linux Applications
#Install flask if necessary
#pip3 install flask

#Run the application
export FLASK_APP=application.py
export FLASK_ENV=development

echo starting the server...
flask run --host=0.0.0.0

