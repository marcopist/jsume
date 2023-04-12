"""Validates the resume.json using the schema."""

import jsonschema
import json


def validate_schema(resume: str) -> str:
    """Validates the schema of the resume json.
    Returns True if the schema is valid, False otherwise.

    args:
        resume (str): The resume json to validate.

    returns:
        str: The error message if the schema is invalid, empty string otherwise.
    """
    with open("resources/schema.json") as f:
        schema = json.load(f)

    resume_dict = json.loads(resume)

    try:
        jsonschema.validate(resume_dict, schema)
        return ""
    except jsonschema.exceptions.ValidationError as e:
        return str(e.message)
