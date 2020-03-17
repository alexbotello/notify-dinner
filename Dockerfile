FROM python:3.7.7-slim-buster

WORKDIR /app

COPY . .

RUN pip install pipenv

RUN pipenv install --system

ENV PORT 8000

CMD ["python", "app.py"]