import requests as re
import json
from ..app.app import app

def get_gists(username):
    res = re.get(
        f"https://api.github.com/users/{username}/gists"
    )
    return json.loads(res.text)

def get_resume_gist_url(github_resp):
    for gist in github_resp:

        files = gist['files']
        if 'resume.json' in files:
            return files['resume.json']['raw_url']

    return None

def get_raw_from_url(url):

    if url is None:
        return None
    
    res = re.get(url)
    data = json.loads(res.text)
    return data

def get_resume_from_username(username):
    gists = get_gists(username)
    app.logger.info(f"Found {len(gists)} gists  for username {username}")
    resume_url = get_resume_gist_url(gists)
    app.logger.info(f"Found {resume_url=} ")
    resume = get_raw_from_url(resume_url)
    return resume

def get_theme_from_gist(username, theme):
    github_resp = get_gists(username)
    if len(github_resp) > 0:
        files = github_resp[0]['files']

        if f'{theme}.jinja' in files:
            return re.get(files[f'{theme}.jinja']['raw_url']).text

    return None