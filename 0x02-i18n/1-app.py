#!/usr/bin/env python3
'''Instantiate the Babel object'''
from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = ["en"]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    return "Hellow World"


if __name__ == '__main__':
    app.run(debug=True)
