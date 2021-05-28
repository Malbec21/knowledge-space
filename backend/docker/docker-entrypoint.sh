#!/bin/bash

if test "$1" == "migrate"; then

    exec /bin/bash -c "python /code/manage.py migrate"

elif  test "$1" == "runserver"; then

    exec /bin/bash -c "python /code/manage.py runserver 0.0.0.0:8000"

elif  test "$1" == "migrate_and_runserver"; then

    exec /bin/bash -c "python /code/manage.py migrate \
        && python /code/manage.py collectstatic \
        && gunicorn src.wsgi:application --bind 0.0.0.0:8000"
else

    echo "Provide a command argument when running the container:"
    echo "  - migrate"
    echo "  - runserver"
    echo "  - migrate_and_runserver"
    echo ""
    echo "You provided: $@"
    exit 1

fi
