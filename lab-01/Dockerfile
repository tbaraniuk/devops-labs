FROM python:3.12-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


FROM python:3.12-slim

RUN useradd --create-home app && mkdir /data && chown app /data

WORKDIR /app

COPY app.py .

USER app

EXPOSE 8080

CMD [ "python", "app.py" ]