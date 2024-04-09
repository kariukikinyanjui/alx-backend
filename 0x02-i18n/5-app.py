#!/usr/bin/env python3
'''Mock loggin in'''
from flask import Flask, render_template, g
from flask_babel import Babel, gettext


app = Flask(__name__)
app.config.from_object('config')


babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    return users.get(user_id)


@app.before_requests
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)


@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)


@app.route('/')
def index():
    if g.user:
        welcome_message = gettext('not_logged_in')
    return render_template('5-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
