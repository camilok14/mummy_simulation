import unittest
from unittest.mock import patch

def insert():
    insert.inserted = True
def purge():
    purge.purged = True
class MockTinyDB():
    def __init__(self):
        insert.inserted = False
        purge.purged = False
        self.doc = {}
    def table(self, name):
        return self
    def update(self, doc):
        for key in doc.keys():
            self.doc[key] = doc[key]
    def get(self, query):
        return self.doc
    def insert(self, doc):
        insert()
        self.doc = doc
    def purge_tables(self):
        purge()

class TestDB(unittest.TestCase):
    @patch('tinydb.TinyDB')
    def setUp(self, TinyDB):
        TinyDB.return_value = MockTinyDB()
        from controller.db import DatabaseController
        self.db_controller = DatabaseController()
    
    def test_current_week(self):
        from controller.db import DatabaseController
        self.db_controller = DatabaseController(True)
        week = 3
        self.db_controller.set_current_week(week)
        current_week = self.db_controller.get_current_week()
        self.assertEqual(current_week, week)
        self.assertTrue(purge.purged)
    
    def test_add_investor(self):
        doc = {'id': 'bla', 'innocence': 0.3, 'experience': -1, 'charisma': 3}
        self.assertRaises(ValueError, self.db_controller.add_investor, doc)
        doc['id'] = 123
        self.assertRaises(ValueError, self.db_controller.add_investor, doc)
        doc['experience'] = 0.45
        self.assertRaises(ValueError, self.db_controller.add_investor, doc)
        doc['charisma'] = 0.5
        self.db_controller.add_investor(doc)
        self.assertTrue(insert.inserted)
        self.assertFalse(purge.purged)

if __name__ == '__main__':
    unittest.main()