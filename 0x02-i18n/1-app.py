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
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> Callable:
    """this method gets the root page of the app"""
    return render_template('1-index.html')
