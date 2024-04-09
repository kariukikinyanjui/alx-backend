#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
app.config['LANGUAGES'] = ["en", "fr"]


babel = Babel(app)

SUPPORTED_LANGUAGES = app.config['LANGUAGES']


@babel.localeselector
def get_locale():
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        if requested_locale in SUPPORTED_LANGUAGES:
            return requested_locale
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


@app.route('/')
def index():
    return render_template('3-index.html', title-gettext(
        'home_title'), header=gettext('home_header'))


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
