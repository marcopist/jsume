[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# resume.json → resume.pdf

**[TOTALLY A WORK IN PROGRESS!]** It does work. But kind of. And everything might get completely reengineered at any point. 🙃

Use with caution for now.

## What it does
As simple as:
- Save your resume as a `resume.json` gist on Github;
- Make sure it conforms to this [schema](https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json);
- Choose the theme you want to use by setting your `$.meta` section in your `resume.json` like this:
    ```
    {
        "meta" : {
            "author" : "{theme-author-name}",
            "name" : "{theme-name}"
        }
        ...
    }
    ```
- Go to `cv.marcopist.com/{your-github-username}`
- Find your cv rendered as a PDF, enjoy!

## What an example looks like
- My [`resume.json`](https://gist.githubusercontent.com/marcopist/619a7ed8bbcde6efa7df28e509d319e7)
- My theme: [`marcopist/basic.jinja`](https://gist.githubusercontent.com/marcopist/1e390f2df03cad92ba21ae78129f679d)
- My rendered [cv.marcopist.com/marcopist](http://cv.marcopist.com/marcopist)

## How to contribute

### Make new themes!
Check out my example theme: [`marcopist/basic.jinja`](https://gist.githubusercontent.com/marcopist/1e390f2df03cad92ba21ae78129f679d). Themes are Jinja templates in HTML. Feel free to add a CSS section in the `<style>` tags in the `<head>`.

### Contribute to the service
Simply make a pull request. I will review it. See the tech specs below on some general architecture notes.

There is continuous integration that runs the unit testing suite whenever any pull request is submitted. See `/tests/Dockerfile` and `.github/workflows/run-tests.yaml` for details.


## Service architecture & design

This is a containerised application (see `/Dockerfile`). Using containers is made necessary by the fact that this application has dependencies that cannot be declared within `setup.cfg` or `pyproject.toml`; the main one being `wkhtmltopdf`, which is allows the generation of a PDF from HTML.

Similarly, the unit testing suite is containerised (see `/tests/Dockerfile`) as it requires `imagemagick` to compare PDFs pixel-wise - in addition to `wkhtmltopdf` to generate them.

This service is deployed to Google Cloud Run. Continuous Deployment is activated, so on every push to `main` the container is re-built & deployed.

Unit testing is run at every pull request using Github workflows (see `/tests/Dockerfile` and `/.github/workflows/run-tests.yaml`).
