FROM python:3
ENV PYTHONUNBUFFERED 1
ARG WORKINGDIR=/code
RUN mkdir -p $WORKINGDIR
WORKDIR $WORKINGDIR
# COPY docker/requirements.txt $WORKINGDIR
COPY requirements.txt $WORKINGDIR
RUN pip install -r requirements.txt
# COPY code/ /code/
# CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
