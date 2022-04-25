# bookstore_api
This is a guided tutorial for creating an API application for a Bookstore.

Start project with the following commands:
```bash
docker-compose run --rm bookstore django-admin startproject project #BUG; move all dirs one up
docker-compose run --rm bookstore django-admin startapp bookstore
docker-compose up -d && docker-compose logs -f bookstore
```

Login to the Jupyter Notebook through:

http://localhost:8888
[password = secret123]


The app will be available at:

http://localhost:8000
