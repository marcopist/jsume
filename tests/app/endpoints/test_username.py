from unittest.mock import patch

from json_resume.app.endpoints.username import route_username

from tests.utils.code.safe_get_gist import safe_get_gist
from tests.utils.code.compare_pdf import compare_pdf


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
