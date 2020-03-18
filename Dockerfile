FROM python:3.7.7-slim-buster

COPY . .

RUN pip install pipenv

RUN pipenv install --system

ENV PORT 5000

WORKDIR /app

CMD ["python", "app.py"]