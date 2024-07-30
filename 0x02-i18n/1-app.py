#!/usr/bin/env python3
"""This file defines the routes"""

from flask import Flask, render_template
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


class Config:
    """This class defines the configuration of the app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """this method gets the root page of the app"""
    return render_template('1-index.html')
