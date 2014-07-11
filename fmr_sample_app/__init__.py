from flask import Flask


def make_app(global_conf, debug = None, **app_conf):
    app = Flask(__name__)

    app.debug = debug.lower() == "true"
    app.config.update(app_conf)

    return app.wsgi_app
