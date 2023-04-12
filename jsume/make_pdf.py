"""Module containing the logics to build the pdf from
a template theme and a parsed resume dictionary."""

from addict import Dict
import pdfkit
from .github import get_theme
from jinja2.sandbox import SandboxedEnvironment
from jsume.app import LOGGER
from typing import Literal

sandbox = SandboxedEnvironment()


def makepdf(resume_raw: Dict, author: str = "", theme: str = "") -> None | bytes:
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

    if theme == "" and author == "":
        author = resume["meta"]["author"]
        theme = resume["meta"]["theme"]

    template = get_theme(author, theme)

    if template is None:
        LOGGER.error("No theme found for %s/%s", author, theme)
        return None

    rendered = sandbox.from_string(template).render(resume=resume)

    pdf: bytes = pdfkit.from_string(rendered, options={"enable-local-file-access": ""})  # type: ignore

    return pdf
