from json_resume.logics.github import get_gist


def test_get_gist():
    expected = "integration ok!"
    actual = get_gist("marcopist", "test_integration.txt")
    assert actual == expected
