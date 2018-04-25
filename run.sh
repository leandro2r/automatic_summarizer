#!/bin/bash

python manage.py migrate --noinput
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@automaticsummarizer', 'qwe123')" | python manage.py shell
python manage.py runserver 0.0.0.0:8080
