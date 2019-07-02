from unittest import main, TestCase
from unittest.mock import patch
from random import choice
from importlib import reload
import simulation

class MockDatabaseController():
    def __init__(self):
        self.investors = {}
        self.members = {}
    def add_investor(self, doc):
        self.investors[doc['id']] = doc
    def get_random_investor(self):
        doc_id = choice(list(self.investors))
        return self.investors[doc_id]
    def add_member(self, investor_id, member_id, week):
        investor = self.investors[investor_id]
        if investor_id == 0: # is the mummy
            member = investor 
            mummy = member
        else:
            member = self.members[member_id]
            mummy = self.members[0]
        investor['week_joined'] = week
        investor['active'] = True
        investor['recruited'] = []
        investor['money'] = 0
        member['recruited'].append(investor_id)
        member['money'] = member['money'] + 100
        mummy['money'] = mummy['money'] + 400
        del self.investors[investor_id]
        self.members[investor_id] = investor
        self.members[member_id] = member
    def set_current_week(self, week):
        self.current_week = week
    def get_current_week(self):
        return self.current_week
    def get_members(self):
        members = []
        for doc_id in self.members:
            members.append(self.members[doc_id])
        return members
    def eliminate_member(self, member_id, week):
        member = self.members[member_id]
        member['active'] = False
        member['week_eliminated'] = week
        self.members[member_id] = member
    def get_mummy_money(self):
        return self.members[0]['money']
class MockLogger:
    def log(self, message):
        pass
class TestSimulation(TestCase):
    @patch('controller.log.Logger')
    @patch('controller.db.DatabaseController')
    def setUp(self, DatabaseController, Logger):        
        DatabaseController.return_value = MockDatabaseController()
        Logger.return_value = MockLogger()
        reload(simulation)
        self.simulation = simulation.Simulation(1000, 0, 'uniform')
    def test_simulation_value_error(self):
        self.assertRaises(ValueError, simulation.Simulation, 1000, 10, 'blabla')
    
    def test_run(self):
        self.simulation.run()

if __name__ == '__main__':
    main()