# syntax=docker/dockerfile:1
FROM python:3.11-slim

# To prevent the ubuntu terminal from
# trying to interact with me
ARG DEBIAN_FRONTEND=noninteractive

# install app dependencies
RUN apt-get update
RUN apt-get install -y wkhtmltopdf imagemagick

# install app
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

# final configuration
CMD python -m pytest