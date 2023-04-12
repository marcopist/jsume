"""This module contains the route for the username endpoint."""

from flask import Response

from jsume.app import app, LOGGER
from jsume.github import get_resume, parse_resume
from jsume.make_pdf import makepdf
from jsume.validate_schema import validate_schema


@app.route("/<username>")
def route_username(username: str) -> str | Response:
    """Returns a pdf of the resume for the given username.

    args:
        username (str): The username to get the resume for.

    returns:
        Response: The pdf of the resume."""
    LOGGER.info(f"{username=}")
    resume = get_resume(username)

    if resume is None:
        LOGGER.warning(f"Can't find gist for {username=}")
        return ""

    validation = validate_schema(resume)
    if validation != "":
        LOGGER.warning(
            f"Resume does not conform to schema for {username=} \n {validation=}"
        )
        return validation

    parsed_resume = parse_resume(resume)

    pdf = makepdf(parsed_resume)

    if pdf is None:
        LOGGER.error(f"Can't generate pdf for {username=}")
        return ""
    else:
        LOGGER.info(f"Generated pdf for {username=}")

    response = Response(
        pdf,
        mimetype="application/pdf",
        headers={"Content-Disposition": "inline;filename=resume.pdf"},
    )

    return response
