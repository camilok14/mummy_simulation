from unittest import main, TestCase
from unittest.mock import patch

def run_server():
    run_server.running = True
class MockDatabaseController():
    def get_mummy_money(self):
        return 1000
    def get_current_week(self):
        return 3
class MockFlask():
    def __init__(self):
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
    def test_mummy_money(self):
        from server import MummyMoney
        health = MummyMoney()
        result = health.get()
        self.assertEqual(result, 1000)
    def test_current_week(self):
        from server import CurrentWeek
        health = CurrentWeek()
        result = health.get()
        self.assertEqual(result, 3)
    def test_server(self):
        self.server.run()
        self.assertTrue(run_server.running)