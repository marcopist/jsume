from jsume.github import get_gist


def test_get_gist() -> None:
    """Test get_gist integration.
    Checks integration with GitHub API."""
    expected = "integration ok!"
    actual = get_gist("marcopist", "test_integration.txt")
    assert actual == expected
