import unittest 
from unittest.mock import patch

from json_resume.app.endpoints.username import route_username

def safe_get_gist(username, file):
    if file == 'resume.json':
        with open("tests/utils/sample-resume.json") as f:
            return f.read()
    elif '.jinja' in file:
        with open("tests/utils/sample-theme.jinja") as f:
            return f.read()
    return None

@patch("json_resume.logics.github.get_gist")
def test_route_username(mock_get_gist):
    mock_get_gist.side_effects = safe_get_gist
    return route_username('test_username')