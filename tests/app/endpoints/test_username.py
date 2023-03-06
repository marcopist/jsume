import unittest
from unittest.mock import patch

from json_resume.app.endpoints.username import route_username
from ...utils.code.compare_pdf import compare_pdf


def safe_get_gist(username: str, file: str) -> str | None:
    """Closure to mock github calls in json_resume.logics.github.get_gist

    NOTE: if `username` == 'noresume' this mocks
    the situation where an user has not published
    a resume to github

    Args:
        username (str): The name of the Github organisation or user
            who published the Gist.
        file (str): The name of the published Gist.

    Returns:
        str | None: the raw file from Github if it exists,
            otherwise it returns `None`.
    """
    if username == "noresume" and file == "resume.json":
        return None
    if file == "resume.json":
        with open("tests/utils/files/inputs/sample-resume.json") as f:
            return f.read()
    elif ".jinja" in file:
        with open("tests/utils/files/inputs/sample-theme.jinja") as f:
            return f.read()
    return None


@patch("json_resume.logics.github.get_gist", safe_get_gist)
def test_route_username_cv_N() -> None:
    """Test for json_resume.app.endpoints.route_username
    Assumes that no resume was published"""
    actual = route_username("noresume")

    assert actual == ""


@patch("json_resume.logics.github.get_gist", safe_get_gist)
def test_route_username_cv_Y() -> None:
    """Test for json_resume.app.endpoints.route_username
    Assumes that a resume was published"""
    with open("tests/utils/files/outputs/sample-resume.pdf", "rb") as f:
        expected_pdf = f.read()

    actual_pdf = route_username("test_username").data

    diff = compare_pdf(expected_pdf, actual_pdf)

    assert diff[1] < 0.01
