#!/usr/bin/env python3
"""
In this task, you will implement a way to force a particular
locale by passing the locale=fr parameter to your app’s URLs
"""
from flask import Flask, render_template, request
from typing import Any
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class that has a LANGUAGES class attribute
    equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("4-app.Config")


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    return index.html template that simply outputs
    “Welcome to Holberton” as page title (<title>) and
    “Hello world” as header (<h1>)
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> Any:
    """
    determine the best match with our supported languages
    """
    if "locale" in request.args:
        if request.args["locale"] in app.config["LANGUAGES"]:
            return request.args["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
