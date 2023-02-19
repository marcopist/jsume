from addict import Dict
from jinja2 import Template
import pdfkit

local_templates = [
    'basic'
]

def handle_local_theme(theme):
    html_path = f'templates/{theme}/resume.html'
    css_path = f'templates/{theme}/resume.css'

    return html_path, css_path
    

def handle_remote_theme(theme):
    # TODO: implement
    return handle_local_theme('basic')

def get_html_css(theme):
    if theme in local_templates:
        return handle_local_theme(theme)
    else:
        return handle_remote_theme(theme)

def makepdf(resume_raw, theme=None):
    resume = Dict(resume_raw)

    if theme == None:
        theme = resume.meta.theme

    html_path, css_path = get_html_css(theme)

    with open(html_path) as f:
        template = Template(f.read())

    rendered = template.render(resume = resume)

    return pdfkit.from_string(
        rendered,
        css=css_path,
        options={"enable-local-file-access": ""}
    )
