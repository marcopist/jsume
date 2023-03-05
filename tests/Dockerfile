# syntax=docker/dockerfile:1
FROM python:3.11-slim

# To prevent apt from trying to interact with me
ARG DEBIAN_FRONTEND=noninteractive

# Install app dependencies
RUN apt-get update
RUN apt-get install -y wkhtmltopdf imagemagick

# Install app
COPY . project
COPY /tests/utils/config/policy.xml /etc/ImageMagick-6/policy.xml
WORKDIR /project

# Setting environment variable for imagemagick configuration
ENV MAGICK_CONFIGURE_PATH /etc/ImageMagick-6/policy.xml

# Installing package and testing requirements
RUN python -m pip install .
RUN python -m pip install -r tests/requirements.txt

# Generating pdf to be used in tests
RUN python tests/utils/code/make_output_cv.py

# No port needs to be exposed for tests

# Test command
CMD tox -c tox.ini