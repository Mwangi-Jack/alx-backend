#!/usr/bin/env python3
"""This file defines the routes"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """this method gets the root page of the app"""
    return render_template('0-index.html',
                           title='Welcome to Holberton', header='Hello world')
