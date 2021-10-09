FROM python:3

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY te43^@=a@z7%h+fdt#0ueon7%wsfemel+lu7(&s^^kter)39q4
ENV DEBUG_VALUE 'True'

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /app