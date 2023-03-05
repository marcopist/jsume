import unittest
from unittest.mock import patch

from json_resume.app.endpoints.username import route_username
from ...utils.code.compare_pdf import compare_pdf


def safe_get_gist(username, file):
    if file == "resume.json":
        with open("tests/utils/files/inputs/sample-resume.json") as f:
            return f.read()
    elif ".jinja" in file:
        with open("tests/utils/files/inputs/sample-theme.jinja") as f:
            return f.read()
    return None


@patch("json_resume.logics.github.get_gist", safe_get_gist)
def test_route_username():
    with open("tests/utils/files/outputs/sample-resume.pdf", "rb") as f:
        expected_pdf = f.read()

    actual_pdf = route_username("test_username").data

    diff = compare_pdf(expected_pdf, actual_pdf)

    print(diff)
    assert diff[1] < 0.001
