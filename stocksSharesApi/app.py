from flask import Flask, Blueprint
from flask_restful import Api, Resource
from . import stocks

def create_app(cli=False):
    app = Flask(__name__, static_folder=None)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(stocks.views.blueprint)