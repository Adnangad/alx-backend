#!/usr/bin/env python3
""" This module initializes a web app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configs the lang"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT__LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the default locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home_pg():
    """ Redirects the user to the homepage"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
