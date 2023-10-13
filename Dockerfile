# syntax=docker/dockerfile:1
FROM python:3.11-slim-bullseye
WORKDIR /app
COPY ./geras_servisas .
COPY ./requirements.txt .
RUN apt update
RUN apt upgrade
RUN pip3 install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "-b", "0.0.0.0:8000", "geras_servisas.wsgi"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

