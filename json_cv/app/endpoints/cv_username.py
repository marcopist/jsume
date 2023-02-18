from flask import Response

from json_cv.app.app import app
from json_cv.logics.github import get_resume_from_username
from json_cv.logics.make_pdf import makepdf

@app.route("/cv/<username>")
def cv_username(username):
    resume = get_resume_from_username(username)

    if resume is None:
        return ''

    file =  makepdf(resume)

    response = Response(
        file,
        mimetype='application/pdf',
        headers = {
            'Content-Disposition' : 'attachment;filename=resume.pdf'
        }
    )

    return response