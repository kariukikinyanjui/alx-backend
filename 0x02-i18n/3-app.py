#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
app.config.from_object('config')

babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('3-index.html', title=gettext(
        'home_title'), header=gettext('home_header'))


if __name__ == '__main__':
    app.run(debug=True)
