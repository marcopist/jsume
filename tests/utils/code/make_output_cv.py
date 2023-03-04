import unittest 
from unittest.mock import patch

from json_resume.app.endpoints.username import route_username

def safe_get_gist(username, file):
    if file == 'resume.json':
        with open("tests/utils/files/inputs/sample-resume.json") as f:
            return f.read()
    elif '.jinja' in file:
        with open("tests/utils/files/inputs/sample-theme.jinja") as f:
            return f.read()
    return None

@patch("json_resume.logics.github.get_gist", safe_get_gist)
def make_test_pdf():
    with open('tests/utils/files/outputs/sample-resume.pdf', 'wb') as f:
        f.write(route_username('test_username').data)

make_test_pdf()