#!/usr/bin/env bash

docker-compose build
docker-compose down -v
docker-compose run --rm bookstore rm -Rf manage.py project bookstore manage.py db.sqlite3
docker-compose run --rm bookstore django-admin startproject project .
docker-compose run --rm bookstore python manage.py startapp bookstore
# docker-compose run --rm bookstore python manage.py createsuperuser
docker-compose up -d --remove-orphans
# docker-compose -f docker-compose_proxy.yml up -d --remove-orphans

docker-compose run --rm jupyter python run_notebooks.py '01 Automation Challenge Book API - Settings.ipynb'
docker-compose run --rm jupyter python run_notebooks.py '02 Automation Challenge Book API - Database.ipynb'
# docker-compose run --rm jupyter python run_notebooks.py '03 Automation Challenge Book API - Models.ipynb'
# docker-compose run --rm jupyter python run_notebooks.py  '04 Automation Challenge Book API - Serialization.ipynb'
# docker-compose run --rm jupyter python run_notebooks.py  '05 Automation Challenge Book API - URLs en Views.ipynb'
# docker-compose run --rm jupyter python run_notebooks.py  '06 Automation Challenge Book API - Pagination.ipynb'

docker-compose logs -f

# Visualise database model
# docker-compose run --rm bookstore python manage.py graph_models -a > bookstore.dot
# dot -Tpng bookstore.dot -o bookstore.png