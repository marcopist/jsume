from flask import Response

from json_resume.app.app import app
from json_resume.logics.github import get_resume_from_username
from json_resume.logics.make_pdf import makepdf

@app.route("/cv/<username>")
def route_cv_username(username):
    resume = get_resume_from_username(username)

    if resume is None:
        return ''

    file =  makepdf(resume)

    response = Response(
        file,
        mimetype='application/pdf',
        headers = {
            'Content-Disposition' : 'inline;filename=resume.pdf'
        }
    )

    return response