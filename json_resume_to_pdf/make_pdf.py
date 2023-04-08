"""Module containing the logics to build the pdf from
a template theme and a parsed resume dictionary"""
from addict import Dict
import pdfkit
from .github import get_theme
from jinja2.sandbox import SandboxedEnvironment
from json_resume_to_pdf.app import LOGGER

sandbox = SandboxedEnvironment()


def makepdf(resume_raw: Dict, author: str = None, theme: str = None) -> bytes:
    """Returns a rendered pdf based on a json resume `resume_raw`.
    Extracts the theme information from the `resume_raw` input, but also
    tolerates explicitly defined temem through the `author` and `theme` arguments.

    Args:
        resume_raw (addict.Dict): Resume data.
        author (str, optional): Author of the theme to be used.
            Defaults to None.
        theme (str, optional): Name of the theme to be used.
            Defaults to None.

    Returns:
        bytes: The bytes of the generated pdf.
    """
    resume = Dict(resume_raw)

    if not (theme and author):
        author = resume.meta.author
        theme = resume.meta.theme

    template = get_theme(author, theme)

    rendered = sandbox.from_string(template).render(resume=resume)

    return pdfkit.from_string(rendered, options={"enable-local-file-access": ""})
