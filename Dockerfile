# syntax=docker/dockerfile:1
FROM python:3.11-slim

# To prevent the ubuntu terminal from
# trying to interact with me
ARG DEBIAN_FRONTEND=noninteractive

# install app dependencies
RUN apt-get update
RUN apt-get install -y wkhtmltopdf

# install app
COPY json_resume project/json_resume
COPY pyproject.toml project/pyproject.toml
COPY setup.cfg project/setup.cfg
COPY setup.py project/setup.py
COPY version.txt project/version.txt
WORKDIR /project

RUN python -m pip install .

# final configuration
EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "json_resume.wsgi:app"]