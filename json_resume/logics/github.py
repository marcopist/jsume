import requests as re
import json
from json_resume.app.app import app


def get_gist(username: str, file: str) -> str | None:
    """Grabs a the content of a Github gist called "file"
    published by an user called "username"

    Args:
        username (str): _description_
        file (str): _description_

    Returns:
        _type_: _description_
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

def get_theme(author, theme):
    return get_gist(author, theme + ".jinja")

def get_resume(username):
    return get_gist(username, "resume.json")


###### Old and irrelevant

def get_resume_from_username(username):
    return json.loads(get_gist(username, 'resume.json'))