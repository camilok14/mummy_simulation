from unittest import main, TestCase
from unittest.mock import patch

def run_server():
    run_server.running = True
class MockDatabaseController():
    def get_members(self):
        return [{}]
    def get_timelapse(self):
        return {'current_week': 3, 'program_ended': False}
    
class MockFlask():
    def __init__(self):
        pass
    def after_request(self, arg1):
        pass
    def run(self, port):
        run_server()
class MockApi():
    def __init__(self, app):
        self.app = app
    def add_resource(self, res, path):
        pass


class TestServer(TestCase):
    @patch('flask.Flask')
    @patch('flask_restful.Api')
    @patch('controller.db.DatabaseController')
    def setUp(self, DatabaseController, Api, Flask):
        run_server.running = False
        DatabaseController.return_value = MockDatabaseController()
        app = MockFlask()
        Flask.return_value = app
        Api.return_value = MockApi(app)
        from server import Server
        self.server = Server()
    def test_health(self):
        from server import Health
        health = Health()
        result = health.get()
        self.assertEqual(result, 'Service is up and running')
    def test_members(self):
        from server import Member
        member = Member()
        result = member.get()
        self.assertEqual(len(result), 1)
    def test_timelapse(self):
        from server import Timelapse
        timelapse = Timelapse()
        result = timelapse.get()
        self.assertEqual(result['current_week'], 3)
        self.assertFalse(result['program_ended'])
    def test_server(self):
        self.server.run()
        self.assertTrue(run_server.running)