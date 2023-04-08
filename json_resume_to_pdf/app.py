"""This module contains the main Flask app: `app`"""

from flask import Flask

app = Flask("json_resume_to_pdf")

LOGGER = app.logger