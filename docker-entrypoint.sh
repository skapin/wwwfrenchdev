#!/bin/sh -e

echo "---> Starting in '$1' mode"

case "$1" in
    dev)
        cd /usr/src/app/
        python manage.py migrate
        exec python manage.py runserver 0.0.0.0:8001
        ;;
    prod)
        python manage.py migrate
        exec gunicorn fboudinetwebsite.wsgi:application -w 2 -b :8000
        ;;
    *)
	echo "Usage: $0 (prod|dev)"
	exit 1
	;;
esac
