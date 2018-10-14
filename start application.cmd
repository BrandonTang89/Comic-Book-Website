pip install flask
set Flask_APP=application.py
set FLASK_ENV=development
:while
echo starting the server...
flask run --host=0.0.0.0
goto :while