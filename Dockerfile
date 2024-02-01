FROM python:3.10-alpine3.16

RUN apk add postgresql-client build-base postgresql-dev

WORKDIR /birzhatruda

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

RUN adduser --disabled-password justuser
USER justuser

COPY . .