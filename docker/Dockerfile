FROM python:3
ENV PYTHONUNBUFFERED 1
ARG WORKINGDIR=/code
RUN mkdir -p $WORKINGDIR
WORKDIR $WORKINGDIR
COPY requirements.txt $WORKINGDIR
RUN pip install -r requirements.txt
