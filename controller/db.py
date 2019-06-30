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