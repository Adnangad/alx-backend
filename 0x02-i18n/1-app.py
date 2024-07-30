#!/usr/bin/env python3
""" This module initializes a web app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configs the lang"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route("/")
def home_pg():
    """ Redirects the user to the homepage"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
