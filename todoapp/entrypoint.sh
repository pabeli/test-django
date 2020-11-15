#!/bin/sh

# Ensure that Postgres is healthy
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate
python manage.py collectstatic --no-input --clear
cp /code/static/admin/admin_colors.css /code/staticfiles/admin/

# Launch the web server
exec "$@"