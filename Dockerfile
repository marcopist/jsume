# syntax=docker/dockerfile:1
FROM python:3.11-slim

# To prevent apt from trying to interact with me
ARG DEBIAN_FRONTEND=noninteractive

# install app dependencies
RUN apt-get update
RUN apt-get install -y wkhtmltopdf

# Install app
COPY jsume project/jsume
COPY resources project/resources
COPY pyproject.toml project/pyproject.toml
COPY setup.cfg project/setup.cfg
COPY setup.py project/setup.py
COPY version.txt project/version.txt
WORKDIR /project

RUN python -m pip install .

# Expose port
EXPOSE 8000

# Run command
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "jsume.wsgi:app"]