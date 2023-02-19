# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y wkhtmltopdf python3 python3-pip 

# install app
COPY json_resume json_resume

RUN pip install -r requirements.txt

# final configuration
EXPOSE 8000
CMD python -m gunicorn --worker-tmp-dir /dev/shm json_resume.wsgi:app