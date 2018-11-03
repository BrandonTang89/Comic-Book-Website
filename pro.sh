#!/bin/bash
#for production running on linux
echo "Starting the Server..."
gunicorn3 application:app -b 0.0.0.0:5000 -w 4
