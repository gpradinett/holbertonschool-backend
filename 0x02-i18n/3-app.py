#!/usr/bin/env python3
"""
Create a get_locale function with the babel.localeselector
decorator. Use request.accept_languages to determine the best match
with our supported languages
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


app.config.from_object("3-app.Config")


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    return index.html template that simply outputs
    “Welcome to Holberton” as page title (<title>) and
    “Hello world” as header (<h1>)
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> Any:
    """
    determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
