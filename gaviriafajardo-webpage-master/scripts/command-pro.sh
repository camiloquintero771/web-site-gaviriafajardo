#!/bin/sh

echo "Installing npm dependencies"
npm install
npm run build
python manage.py collectstatic --no-input
gunicorn -b :9000 -w 3 gaviriafajardo.wsgi:application --reload --timeout 3600
