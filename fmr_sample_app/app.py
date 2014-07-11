from flask import Flask
from flask.ext.metaroute import MetaRoute
from . import controllers

def make_app(global_conf, **app_conf):
    app = Flask(__name__)
    app.config.update(app_conf)

    MetaRoute(app, controllers)

    return app.wsgi_app
