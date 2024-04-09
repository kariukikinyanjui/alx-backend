#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locals():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True)
