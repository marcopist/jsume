# syntax=docker/dockerfile:1
FROM python:3.9

# To prevent the ubuntu terminal from
# trying to interact with me
ARG DEBIAN_FRONTEND=noninteractive

# install app dependencies
RUN apt-get update
RUN apt-get install -y wkhtmltopdf

# install app
COPY . project
WORKDIR /project

RUN python -m pip install -e .

# final configuration
EXPOSE 8000

CMD python json_resume
#CMD python -m gunicorn --worker-tmp-dir /dev/shm json_resume.wsgi:app