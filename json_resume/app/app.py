from flask import Flask

app = Flask(
    "json_resume",
    template_folder='/project/json_resume/app/templates',
    static_folder='/project/json_resume/app/static'
)