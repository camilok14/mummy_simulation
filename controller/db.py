from tinydb import TinyDB, Query
from random import choice

class DatabaseController:
    """
    Class with the responsability of managing exchanges with the database.
    """
    def __init__(self, purge = False):
        """
        Constructor of an instance of the controller.
        Parameters
        ----------
        purge : bool
            When true, will erase all data in the database, to start a clean simulation.
        """
        self.db = TinyDB('./db.json')
        if purge:
            self.db.purge_tables()
        self.investors = self.db.table('investors')
        self.members = self.db.table('members')
    def add_investor(self, investor_doc) -> None:
        """
        Insert a new investor in the universe of candidates to join the program.
        This method should not be called during the simulation, but when preparing the universe to start the simulation.
        Parameters
        ----------
        investor_doc : dict
            Document representing the investor, must have the keys id (int), innocence (float between 0 and 1),
            experience (float between 0 and 1), charisma (float between 0 and 1).
        """
        if not isinstance(investor_doc['id'], int):
            raise ValueError('id must be an unique int')
        for x in ['innocence', 'experience', 'charisma']:
            if investor_doc[x] > 1 or investor_doc[x] < 0:
                raise ValueError('Attributes must be between 0 and 1')
        self.investors.insert(investor_doc)
    def set_current_week(self, current_week) -> None:
        """
        Sets the value of the simulation's current week.
        Parameters
        ----------
        current_week : int
            The desired value to set as the current week.
        """
        self.db.update({'current_week': current_week})
    def get_current_week(self) -> int:
        """
        Returns the value of the simulation's current week.
        """
        return self.db.get(Query())['current_week']