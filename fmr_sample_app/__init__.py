from flask import Flask


def make_app(global_conf, **app_conf):
    app = Flask(__name__)
    app.config.update(app_conf)
    return app
