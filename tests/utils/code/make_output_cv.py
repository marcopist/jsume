import json
from addict import Dict
from jinja2.sandbox import SandboxedEnvironment
import pdfkit

sandbox = SandboxedEnvironment()

with open("tests/utils/files/inputs/sample-resume.json", "r") as f:
    resume_raw = json.loads(f.read())

with open("tests/utils/files/inputs/sample-theme.jinja", "r") as f:
    template = f.read()

resume = Dict(resume_raw)
rendered = sandbox.from_string(template).render(resume=resume)

with open("tests/utils/files/outputs/sample-resume.pdf", "wb") as f:
    f.write(
        pdfkit.from_string(
            rendered,
            #'tests/utils/outputs/sample-resume.pdf',
            options={"enable-local-file-access": ""},
        )
    )
