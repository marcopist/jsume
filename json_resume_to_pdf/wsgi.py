"""WSGI entry point for the application."""

from json_resume_to_pdf.app import app, LOGGER
from json_resume_to_pdf.endpoints import *
import logging


if __name__ == "__main__":
    LOGGER.setLevel(logging.INFO)
    app.run()
