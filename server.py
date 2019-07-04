from flask import Flask, request
from flask_restful import Resource, Api
from controller.db import DatabaseController
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        @self.app.after_request
        def after_request(response): #pylint: disable=unused-variable
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            return response
        api = Api(self.app)
        api.add_resource(Health, '/health')
        api.add_resource(Timelapse, '/timelapse')
        api.add_resource(Member, '/members')
        api.add_resource(Investors, '/investors')
    def run(self):
        self.app.run(host = '0.0.0.0', port = '3030')

class Health(Resource):
    def get(self):
        return 'Service is up and running'
class Member(Resource):
    def get(self):
        return DatabaseController().get_members()
class Timelapse(Resource):
    def get(self):
        return DatabaseController().get_timelapse()
class Investors(Resource):
    def get(self):
        return DatabaseController().count_investors()
