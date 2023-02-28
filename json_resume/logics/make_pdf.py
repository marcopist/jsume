from addict import Dict
from jinja2 import Template
import pdfkit
from .github import get_theme_from_gist
from jinja2.sandbox import SandboxedEnvironment

sandbox = SandboxedEnvironment()

def makepdf(resume_raw, theme=None):
    resume = Dict(resume_raw)

    if theme == None:
        author = resume.meta.author
        theme = resume.meta.theme

    template = get_theme_from_gist(author, theme)

    rendered = sandbox.from_string(template).render(resume = resume)

    return pdfkit.from_string(
        rendered,
        options={"enable-local-file-access": ""}
    )
