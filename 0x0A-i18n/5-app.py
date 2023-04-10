#!/usr/bin/env python3
"""  Lorem ipsum dolor sit amet, consectetur   """
from flask_babel import Babel, _
from flask import Flask, render_template, request, g
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """  Lorem ipsum dolor sit amet, consectetur  """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """  Lorem ipsum dolor sit amet, consectetur  """

    try:
        login_as = request.args.get("login_as")
        user = users[int(login_as)]
    except Exception:
        user = None

    return user


@app.before_request
def before_request():
    """ Operations that happen before any request """
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a Basic Template for Babel Implementation"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """Select a language translation to use for that request"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
