#!/usr/bin/env python3
""" Lorem ipsum dolor sit amet, consectetur adipiscing elit """
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Lorem ipsum dolor sit amet, consectetur  """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """lorem  Lorem ipsum dolor sit amet, consectetur  """
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """ Lorem ipsum dolor sit amet, consectetur  """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
