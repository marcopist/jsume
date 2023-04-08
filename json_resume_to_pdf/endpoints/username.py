from flask import Response

from json_resume_to_pdf.app import app, LOGGER
from json_resume_to_pdf.github import get_resume, parse_resume
from json_resume_to_pdf.make_pdf import makepdf
from json_resume_to_pdf.validate_schema import validate_schema


@app.route("/<username>")
def route_username(username):
    LOGGER.info(f"{username=}")
    resume = get_resume(username)

    if resume is None:
        LOGGER.warning(f"Can't find gist for {username=}")
        return ""

    validation = validate_schema(resume)
    if validation != "":
        LOGGER.warning(f"Resume does not conform to schema for {username=} \n {validation=}")
        return validation

    parsed_resume = parse_resume(resume)

    file = makepdf(parsed_resume)

    response = Response(
        file,
        mimetype="application/pdf",
        headers={"Content-Disposition": "inline;filename=resume.pdf"},
    )

    return response
