import jsonschema
import json

## Validate the schema
def validate_schema(resume_str):
    """Validates the schema of the resume json.
    Returns True if the schema is valid, False otherwise.
    
    args:
        resume_json (dict): The resume json to validate.
        
    returns:
        str: The error message if the schema is invalid, empty string otherwise.
    """
    with open('resources/schema.json') as f:
        schema = json.load(f)

    resume = json.loads(resume_str)
    
    try:
        jsonschema.validate(resume, schema)
        return ""
    except jsonschema.exceptions.ValidationError as e:
        return e.message