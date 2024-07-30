#!/usr/bin/env python3

from flask import Flask, render_template, request

from flask_babel import Babel

app = Flask(__name__)

def get_locale():
    """gets the language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(locale_selector=get_locale)


@app.route('/')
def index():
    """this method gets the root page of the app"""
    return render_template('0-index.html', title='Welcome to Holberton', header='Hello world')
