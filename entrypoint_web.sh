#!/bin/bash

python manage.py collectstatic --noinput;
python manage.py migrate
gunicorn -c jt/gunicorn.conf.py jt.wsgi:application