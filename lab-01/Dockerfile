FROM python:3.12-slim as builder

WORKDIR /app

RUN python -m venv /venv

COPY requirements.txt .

RUN /venv/bin/pip install --no-cache-dir -r requirements.txt


FROM python:3.12-slim

RUN useradd --create-home app && mkdir /data && chown app /data

COPY --from=builder /venv /venv

WORKDIR /app

COPY app.py .

USER app

EXPOSE 8080

CMD [ "/venv/bin/python", "app.py" ]