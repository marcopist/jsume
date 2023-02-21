from flask import Response, render_template

from json_resume.app.app import app

@app.route("/cv")
def route_cv():
    return render_template('cv.html')