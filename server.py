from flask import Flask, request
from flask_restful import Resource, Api
from controller.db import DatabaseController

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        @self.app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            return response
        api = Api(self.app)
        api.add_resource(Health, '/health')
        api.add_resource(MummyMoney, '/mummy_money')
        api.add_resource(CurrentWeek, '/current_week')
    def run(self):
        self.app.run(port = '3030')

class Health(Resource):
    def get(self):
        return 'Service is up and running'
class MummyMoney(Resource):
    def get(self):
        db_controller = DatabaseController()
        return db_controller.get_mummy_money()
class CurrentWeek(Resource):
    def get(self):
        db_controller = DatabaseController()
        return db_controller.get_current_week()

