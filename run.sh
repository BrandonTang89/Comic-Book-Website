#!/bin/bash
#Use for Linux Applications

#Install flask if necessary
pip install flask

#Run the application
export FLASK_APP=application.py
export FLASK_ENV=development
while true
do
echo starting the server...
flask run --host=0.0.0.0
done