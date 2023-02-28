from flask import Flask

app = Flask(
    "json_resume",
    template_folder='app/templates',
    static_folder='app/static'
)