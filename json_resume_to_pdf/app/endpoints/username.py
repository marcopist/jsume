from flask import Response

from json_resume_to_pdf.app.app import app, logger
from json_resume_to_pdf.logics.github import get_resume
from json_resume_to_pdf.logics.make_pdf import makepdf
from json_resume_to_pdf.logics.validate_schema import validate_schema


@app.route("/<username>")
def route_username(username):
    logger.info(f"{username=}")
    resume = get_resume(username)

    if resume is None:
        logger.warn(f"Can't find gist for {username=}")
        return ""

    validation = validate_schema(resume)
    if validation != "":
        logger.warn(f"Invalid schema for {username=}")
        return validation

    file = makepdf(resume)

    response = Response(
        file,
        mimetype="application/pdf",
        headers={"Content-Disposition": "inline;filename=resume.pdf"},
    )

    return response
