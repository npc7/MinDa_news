# -*- coding: utf-8 -*-
from config import config
from flask import Flask
from flask.ext.mysql import MySQL

db = MySQL()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from .main import main as main_blueprint
    from .news import news as new_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(new_blueprint, url_prefix='/news/api')
    return app
