"""This module contains the integration logics with Github
which are used to collect resumes and themes."""

import requests as re
import json
import datetime
from jsume.app import LOGGER


def get_gist(username: str, file: str) -> str | None:
    """Grabs a the content of a Github Gist called `file`
        published by a user called `username` if it exists.
        Otherwise it returns `None`.

    Args:
        username (str): The name of the Github organisation or user
            who published the Gist.
        file (str): The name of the published Gist.

    Returns:
        str | None: the raw file from Github if it exists,
            otherwise it returns `None`.
    """
    res = re.get(f"https://api.github.com/users/{username}/gists")
    ghres = json.loads(res.text)

    url = None
    for gist in ghres:
        published_files = gist["files"]
        if file in published_files:
            url = published_files[file]["raw_url"]
            break

    if not url:
        return None  # pragma: no cover

    return re.get(url).text


def get_theme(author: str, theme: str) -> str | None:
    """Grabs the `theme`.jinja published as a Github Gist by user `author`
        if it exists. Otherwise it returns `None`.

    Args:
        author (str): The name of the Github organisation or user
            who published the theme.
        theme (str): The name of the theme.

    Returns:
        str | None: The Jinja template of the theme if it exists,
            otherwise it returns None.
    """
    file_jinja = get_gist(author, theme + ".jinja")
    if file_jinja:
        return file_jinja
    else:
        return get_gist(author, theme + ".jinja.html")


def get_resume(username: str) -> str | None:
    """Grabs the resume.json published as a Gist by user `username`
        if it exists. Otherwise it returns `None`.


    Args:
        username (str): The name of the Github organisation or user
            who published the resume.

    Returns:
        str | None: The parsed resume.json if it exists,
            otherwise it returns `None`.
    """
    gist = get_gist(username, "resume.json")
    if gist:
        return gist


def parse_resume(resume: str) -> dict:
    """Parses the resume json and converts the dates to date objects.

    Args:
        resume (str): The resume json.

    Returns:
        dict: The parsed resume json.
    """
    return json.loads(resume, object_hook=date_hook)


def date_hook(json_dict):
    for key, value in json_dict.items():
        if key in {"startDate", "endDate"}:
            # Convert to date object
            json_dict[key] = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    return json_dict
