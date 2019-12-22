FROM python:3.5
RUN mkdir -p /usr/src/app
COPY ./app/ /usr/src/app
COPY docker-entrypoint.sh /

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput

ENTRYPOINT ["/docker-entrypoint.sh"]