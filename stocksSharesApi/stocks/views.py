from flask import Blueprint
from flask_restful import Api

from .resources import Home, Stock, AddStock


blueprint = Blueprint('stocks', __name__, url_prefix='/api')
stocksBP = Api(blueprint)


stocksBP.add_resource(Home, '/')
stocksBP.add_resource(Stock, '/uuid')
stocksBP.add_resource(AddStock, '/addStock/<string:input>')

