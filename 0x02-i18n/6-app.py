#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, request
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config.from_object('config')

babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    return users.get(user_id)

@babel.localeselector
def get_locale():
    # Locale from URL parameters
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # Locale from user settings
    if hasattr(g, 'user') and g.user and 'locale' in g.user:
        user_locale = g.user['locale']
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # Locale from request header
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@app.before_request
def before_request():
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)

@app.route('/')
def index():
    if g.user:
        welcome_message = gettext('logged_in_as') % {'username': g.user['name']}
    else:
        welcome_message = gettext('not_logged_in')
    return render_template('5-index.html', welcome_message=welcome_message)

if __name__ == '__main__':
    app.run(debug=True)
