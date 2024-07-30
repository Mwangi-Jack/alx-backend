#!/usr/bin/env python3
"""This file defines the routes"""

from typing import Callable
from flask import Flask, render_template
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> Callable:
    """this method gets the root page of the app"""
    return render_template('1-index.html')
