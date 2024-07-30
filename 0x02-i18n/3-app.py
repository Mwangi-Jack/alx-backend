#!/usr/bin/env python3
"""This file defines the routes"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
# app.config.from_object(Config)
babel = Babel(app)


class Config:
    """This class defines the configuration of the app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """this method gets the root page of the app"""
    home_title = gettext('Welcome to Holberton')
    home_header = gettext('Hello world!')
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header)


@babel.localeselector
def get_locale():
    """Gets the locale language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
