#!/usr/bin/env python3
"""This file defines the routes"""

from flask import Flask, render_template, request
from flask_babel import Babel

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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Gets the locale language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
