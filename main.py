import json
from attrdict import AttrDict
from jinja2 import Template
from datetime import datetime
import os
import pdfkit
import shutil

# Read cv json
with open('data/cv.json') as f:
    resume = AttrDict(json.load(f))

style = resume.meta.theme

# Read cv template
with open(f'templates/{style}/resume.html') as f:
    template = Template(f.read())

# Clear output folder
shutil.rmtree("output")
os.makedirs("output")

# Render template
rendered = template.render(resume = resume)

# Decide subfolder name
now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
name = resume.basics.name.lower().replace(" ", "")
subfolder = f"{name}-{now}"
path = "output/" + subfolder + "/"

# Create subfolder
if not os.path.isdir(path):
    os.mkdir(path)

pdfkit.from_string(
    rendered,
    path + "resume.pdf",
    css="templates/basic/resume.css",
    options={"enable-local-file-access": ""}
)