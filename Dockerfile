FROM mcr.microsoft.com/devcontainers/python:0-3.11

RUN pip install Django

COPY mysite mysite

WORKDIR mysite

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80", "--no-reload" ]