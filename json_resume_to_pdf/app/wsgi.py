from json_resume_to_pdf.app.app import app, logger
from json_resume_to_pdf.app.endpoints import *
import logging


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    app.run()
