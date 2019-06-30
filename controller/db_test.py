import unittest
from unittest.mock import patch

class MockTinyDB():
    def __init__(self):
        self.doc = {}
    def table(self, name):
        return self
    def update(self, doc):
        for key in doc.keys():
            self.doc[key] = doc[key]
    def get(self, query):
        return self.doc

class TestDB(unittest.TestCase):
    @patch('tinydb.TinyDB')
    def setUp(self, TinyDB):
        TinyDB.return_value = MockTinyDB()
        from controller.db import DatabaseController
        self.db_controller = DatabaseController()
    
    def test_current_week(self):
        week = 3
        self.db_controller.set_current_week(week)
        current_week = self.db_controller.get_current_week()
        self.assertEqual(current_week, week)

if __name__ == '__main__':
    unittest.main()