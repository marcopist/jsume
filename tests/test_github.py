from unittest.mock import patch
import pytest

from jsume.github import get_gist, get_theme, get_resume
from tests.utils.code.safe_get_gist import safe_get_gist


@pytest.mark.parametrize("username, expected", [("noresume", None)])
@patch("jsume.github.get_gist", safe_get_gist)
def test_get_resume(username, expected):
    assert get_resume(username) == expected
