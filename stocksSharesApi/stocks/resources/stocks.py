from flask import Blueprint, jsonify, request
from flask_restful import Resource
import uuid

class Home(Resource):
    def get(self):
        """home page"""
        return 'server is running colmerapi'

class Stock(Resource):
    def get(self):
        return jsonify(
            {
                "id": uuid.uuid4()
            }
        )
class AddStock(Resource):
    #e.g. /uuid/XXXX where XXXX is anything that you try to ask for in api and you capture what XXXX is and log it.
    #@app.route('/uuid/<string:input>', methods=['GET','POST'])
    def post(self, input):
        print(input)
        return jsonify({'user':input})