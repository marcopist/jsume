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
