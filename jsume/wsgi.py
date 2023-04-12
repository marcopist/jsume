"""WSGI entry point for the application."""

from jsume.app import app, LOGGER
from jsume.endpoints import *
import logging


if __name__ == "__main__":
    LOGGER.setLevel(logging.INFO)
    app.run()
