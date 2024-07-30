#!/usr/bin/env python3
"""This file defines the routes"""

from typing import Callable
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> Callable:
    """this method gets the root page of the app"""
    return render_template('0-index.html')
