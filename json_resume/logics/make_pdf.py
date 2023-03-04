from addict import Dict
import pdfkit
from .github import get_theme
from jinja2.sandbox import SandboxedEnvironment
from json_resume.app.app import app

sandbox = SandboxedEnvironment()

def makepdf(resume_raw, author=None, theme=None):
    resume = Dict(resume_raw)
    app.logger.debug(f"{resume=}")

    if not (theme and author):
        author = resume.meta.author
        theme = resume.meta.theme

    app.logger.info(f"Theme author {author}")
    app.logger.info(f"Theme name = {theme}")

    template = get_theme(author, theme)
    app.logger.debug(f"{template=}")

    rendered = sandbox.from_string(template).render(resume = resume)
    app.logger.debug(f"{rendered=}")

    return pdfkit.from_string(
        rendered,
        options={"enable-local-file-access": ""}
    )
