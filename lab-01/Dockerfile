FROM python:3.12-slim

RUN useradd --create-home app

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

USER app

EXPOSE 8080

CMD [ "python", "app.py" ]