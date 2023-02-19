from json_resume.app.app import app
from json_resume.app.endpoints.cv_username import cv_username

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000)