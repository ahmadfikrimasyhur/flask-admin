from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Initialize babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    if override := request.args.get('lang'):
        session['lang'] = override

    return session.get('lang', 'en')


import admin.main
