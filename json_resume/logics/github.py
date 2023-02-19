import requests as re
import json

def get_gists(username):
    res = re.get(
        f"https://api.github.com/users/{username}/gists"
    )
    return json.loads(res.text)

def get_resume_gist_url(github_resp):
    if len(github_resp) > 0:
        files = github_resp[0]['files']

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
    resume_url = get_resume_gist_url(gists)
    resume = get_raw_from_url(resume_url)
    return resume