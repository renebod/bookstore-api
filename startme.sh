#!/usr/bin/env bash

docker-compose build
docker-compose run --rm bookstore django-admin startproject project .
docker-compose run --rm bookstore python manage.py startapp bookstore
# docker-compose run --rm bookstore python manage.py createsuperuser
docker-compose up -d --remove-orphans
# docker-compose -f docker-compose_proxy.yml up -d --remove-orphans
docker-compose logs -f

# Visualise database model
# docker-compose run --rm bookstore python manage.py graph_models -a > bookstore.dot
# dot -Tpng bookstore.dot -o bookstore.png