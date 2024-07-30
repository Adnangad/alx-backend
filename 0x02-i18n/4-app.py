#!/usr/bin/env python3
""" This module initializes a web app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configures the language and locale"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets the best match for the user's locale."""
    locale = request.args.get('locale', '').strip()
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def home_pg():
    """Renders the home page."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
