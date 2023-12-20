FROM python:3.9-slim

WORKDIR /opt/puzzle-api

ARG MONGO_URL
ARG MONGO_DB_NAME

ENV MONGO_URL=$MONGO_URL
ENV MONGO_DB_NAME=$MONGO_DB_NAME

ADD . /opt/puzzle-api

USER root

RUN pip install -r /opt/puzzle-api/requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
