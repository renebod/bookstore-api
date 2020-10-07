#!/usr/bin/env bash

docker-compose build
docker-compose run --rm bookstore django-admin startproject project .
docker-compose run --rm bookstore python manage.py startapp bookstore_api
# docker-compose run --rm bookstore python manage.py createsuperuser
docker-compose up -d
docker-compose logs -f
