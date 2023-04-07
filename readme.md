[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# JSON Resume -> .pdf

[TOTALLY A WORK IN PROGRESS!] It does work. But kind of. And everything might get completely reengineered at any point. 🙃

Use with caution for now.

## What it does
As simple as:
- Save your resume as a `resume.json` gist on Github;
- Make sure it conforms to this [schema](https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json);
- Choose the theme you want to use by setting your `$.meta` section in your `resume.json` like this:
    ```
    {
        "meta" : {
            "author" : "[theme-author-name]",
            "name" : "[theme-name]"
        }
        ...
    }
    ```
- Go to `cv.marcopist.com/{your-github-username}`
- Find your cv rendered as a pdf, enjoy!

## What an example looks like
- My [`resume.json`](https://gist.githubusercontent.com/marcopist/619a7ed8bbcde6efa7df28e509d319e7/raw/resume.json)
- My theme: [`marcopist/basic.jinja`](https://gist.githubusercontent.com/marcopist/1e390f2df03cad92ba21ae78129f679d/raw/basic.jinja)
- My rendered [`cv.pdf`](https://json-resume-to-pdf-7dkwlpyqqa-ew.a.run.app/marcopist)

## How to contribute

### Make new themes!
Check out my example theme: [`marcopist/basic.jinja`](https://gist.githubusercontent.com/marcopist/1e390f2df03cad92ba21ae78129f679d/raw/basic.jinja). Themes are Jinja templates in HTML. Feel free to add a CSS section in the `<style>` tags above.

### Contribute to the service
Simply make a pull request. I will review it. See the tech specs below on some general architecture notes.


## Service architecture & design

[TBD]