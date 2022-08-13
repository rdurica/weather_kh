#!/bin/bash
cd /app

echo "----- Collect static files ------ "
python3 manage.py collectstatic --noinput

# echo "-----------Apply migration--------- "
# python3 manage.py makemigrations
# python3 manage.py migrate

echo "-----------Run gunicorn--------- "
python3 -m gunicorn -c config/gunicorn.py
