import unittest 
from unittest.mock import patch

from json_resume.app.endpoints.username import route_username

@patch("json_resume.logics.github.")
def test_route_username():
    pass