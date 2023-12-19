FROM python:3.9-slim

WORKDIR /opt/puzzle-api

ARG MONGO_URL

ENV MONGO_URI=$MONGO_URL

ADD . /opt/puzzle-api

USER root

RUN pip install -r /opt/puzzle-api/requirements.txt

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
