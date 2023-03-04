from json_resume.app.app import app
from json_resume.app.endpoints import *
import logging


if __name__ == "__main__":
   app.logger.setLevel(logging.INFO)
   app.run()