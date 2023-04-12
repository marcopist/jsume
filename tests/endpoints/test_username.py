from unittest.mock import patch
from pytest import mark

from flask import Response

from jsume.endpoints.username import route_username

from tests.utils.code.safe_get_gist import safe_get_gist
from tests.utils.code.compare_pdf import compare_pdf


@patch("jsume.github.get_gist", safe_get_gist)
def test_route_username_not_published() -> None:  # type: ignore
    """Test for json_resume.app.endpoints.route_username
    Assumes that no resume was published"""
    actual = route_username("noresume")

    assert actual == ""


@patch("jsume.github.get_gist", safe_get_gist)
def test_route_username_invalid_schema() -> None:  # type: ignore
    """Test for json_resume.app.endpoints.route_username
    Assumes that no resume was published"""
    actual = route_username("invalid_schema")

    assert type(actual) == str
    assert len(actual) > 0


@patch("jsume.github.get_gist", safe_get_gist)
def test_route_username_valid() -> None:  # type: ignore
    """Test for json_resume.app.endpoints.route_username
    Assumes that a resume was published"""
    with open("tests/utils/files/outputs/sample-resume.pdf", "rb") as f:
        expected_pdf = f.read()

    resp = route_username("test_username")

    if type(resp) == Response:
        actual_pdf = resp.data
        assert compare_pdf(expected_pdf, actual_pdf), "PDFs are not the same"
    else:
        assert False, "Unexpected response"
