#!/bin/bash

python manage.py collectstatic --noinput;
gunicorn -c jt/gunicorn.conf.py jt.wsgi:application
