#!/usr/bin/env python3
from typing import Any
from flask_babel import Babel
from flask import Flask, render_template
"""
Basic Babel setup
"""


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
    return template of 1-index.html
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
