FROM python:latest

RUN useradd -ms /bin/bash blitzkrieg

USER blitzkrieg

ENV PYTHONUNBUFFERED 1

WORKDIR /home/blitzkrieg/app

ENV PATH $PATH:/home/blitzkrieg/.local/bin

COPY requirements.txt /home/blitzkrieg/app/

RUN pip install -r requirements.txt

COPY . /home/blitzkrieg/app/