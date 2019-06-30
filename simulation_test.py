from unittest import main, TestCase
from unittest.mock import patch

class MockDatabaseController(object):
    def add_investor(self, doc):
        pass
class TestSimulation(TestCase):
    @patch('controller.db.DatabaseController')
    def setUp(self, DatabaseController):
        DatabaseController.return_value = MockDatabaseController()
        from simulation import Simulation
        self.simulation = Simulation(1000, 10, 'normal')

if __name__ == '__main__':
    main()