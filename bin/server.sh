#!/bin/sh
cd ..
gunicorn --bind 0.0.0.0:5000 main.wsgi:app
