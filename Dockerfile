# syntax=docker/dockerfile:1
FROM python:3.11-slim

# To prevent apt from trying to interact with me
ARG DEBIAN_FRONTEND=noninteractive

# install app dependencies
RUN apt-get update
RUN apt-get install -y wkhtmltopdf

# Install app
COPY json_resume_to_pdf project/json_resume_to_pdf
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
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "json_resume_to_pdf.app.wsgi:app"]