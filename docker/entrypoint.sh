#!/bin/sh

while [ true ]; do
    python manage.py makemigrations
    if [ $? -eq 0 ]; then

        python manage.py migrate
        if [ $? -eq 0 ]; then
            break
        fi

    fi
    sleep 5
done

echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@automaticsummarizer', 'abc123')" | python manage.py shell

python manage.py runserver 0.0.0.0:8080
