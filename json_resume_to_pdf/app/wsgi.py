from json_resume_to_pdf.app.app import app
from json_resume_to_pdf.app.endpoints import *
import logging


if __name__ == "__main__":
    app.logger.setLevel(logging.INFO)
    app.run()
