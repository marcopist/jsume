from json_resume_to_pdf.validate_schema import validate_schema
import pytest
from unittest import mock

valid_resume = """
    {
        "basics":{
            "name":"John Doe",
            "label":"Programmer"
        }
    }
"""

# This resume is invalid because it has an extra key: "fitness"
invalid_resume = """
    {
        "basics":{
            "name":"John Doe",
            "label":"Programmer"
        },
        "fitness":"good"
    }
""" 

@pytest.mark.parametrize("resume, valid", [(valid_resume, True), (invalid_resume, False)])
def test_validate_schema(resume, valid):
    """Test validate_schema.
    
    NB: need to mock jsonschema.validate because it is not
    possible to test the schema without a network connection.
    The schema used references a URL."""
    with mock.patch("jsonschema.validate") as mock_validate:
        if valid:
            assert validate_schema(resume) == ""
        else:
            mock_validate.side_effect = Exception("Invalid schema")
            with pytest.raises(Exception) as excinfo:
                validate_schema(resume)
            assert "Invalid schema" in str(excinfo.value)
        