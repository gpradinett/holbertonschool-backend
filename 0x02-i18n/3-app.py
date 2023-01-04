#!/usr/bin/env python3
"""
Basic Babel setup
"""
from typing import Any
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    class config language to 'en', 'fr'
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index() -> Any:
    """
    return template of 3-index.html
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> Any:
    """
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
