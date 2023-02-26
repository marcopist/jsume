from flask import Response, render_template

from json_resume.app.app import app

@app.route("/")
def route_home():
    return render_template('cv.html')