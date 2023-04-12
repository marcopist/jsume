"""This module contains the main Flask app: `app`."""

from flask import Flask

app = Flask("jsume")

LOGGER = app.logger
