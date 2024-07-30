#!/usr/bin/env python3
"""This file defines the routes"""

from typing import Callable
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """This class defines the configuration of the app"""

    LANGUAGES = ['en', 'fr']


app.config['DEFAULT_LOCALE'] = "en"
app.config['DEFAULT_TIMEZONE'] = "UTC"


@app.route('/')
@app.config
def index() -> Callable:
    """this method gets the root page of the app"""
    return render_template('0-index.html')
