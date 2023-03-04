from flask import Response

from json_resume.app.app import app
from json_resume.logics.github import get_resume
from json_resume.logics.make_pdf import makepdf

@app.route("/<username>")
def route_username(username):
    app.logger.info(f"{username=}")
    resume = get_resume(username)


    if resume is None:
        app.logger.warn(f"Can't find gist for {username=}")
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