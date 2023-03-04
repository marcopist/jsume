import requests as re
import json
from json_resume.app.app import app


def get_gist(username: str, file: str) -> str | None:
    """Grabs a the content of a Github gist called "file"
    published by an user called "username"

    Args:
        username (str): The name of the Github organisation or user
            who published the gist
        file (str): the name of the published gist

    Returns:
        str | None: the raw file from Github if it exists,
            otherwise it returns None 
    """
    res = re.get(
        f"https://api.github.com/users/{username}/gists"
    )
    ghres = json.loads(res.text)

    url = None
    for gist in ghres:
        published_files = gist['files']
        if file in published_files:
            url = published_files[file]['raw_url']
            break

    if not url:
        return None
    
    return re.get(url).text

def get_theme(author: str, theme: str) -> str | None:
    """Grabs a the "theme.jinja" published as a gist by user "author"

    Args:
        author (str): The name of the Github organisation or user
            who published the theme
        theme (str): the name of the theme

    Returns:
        str | None: the Jinja template of the theme if it exists,
            otherwise it returns None 
    """
    return get_gist(author, theme + ".jinja")

def get_resume(username: str) -> str | None:
    """Grabs a the "resume.json" published as a gist by user "username"


    Args:
        username (str): The name of the Github organisation or user
            who published the resume

    Returns:
        str | None: the parsed resume.json if it exists,
            otherwise it returns None 
    """
    return json.loads(get_gist(username, 'resume.json'))