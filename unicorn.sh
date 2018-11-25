#!/bin/bash

export DJANGO_SETTINGS_MODULE=orderForm.settings

cd orderForm/
#exec gunicorn --threads 3 -w 3 -b 0.0.0.0:8000 orderForm.wsgi:application
exec gunicorn --reload --reload-engine="auto" --ca-certs=/usr/share/ca-certificates/-.vectronic-wildlife.com_ssl_certificate_INTERMEDIATE.cer --certfile=/usr/share/ca-certificates/vectronic-wildlife.com_ssl_certificate.cer --keyfile=/usr/share/ca-certificates/_.vectronic-wildlife.com_private_key.key --threads 3 -w 3 -b 0.0.0.0:443 orderForm.wsgi:application

exec "$@"