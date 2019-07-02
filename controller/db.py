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
    def get_random_investor(self) -> dict:
        """
        Returns a random investor document from the universe of investors.
        """
        return choice(self.investors.all())
    def add_member(self, investor_id, member_id, current_week) -> None:
        """
        Adds a new member to the Mummy Money, Get Rich Quick Program!
        Parameters
        ----------
        investor_id : int
            The id of the investor that will become a member.
        member_id: int
            The id of the member that invited the investor to become a member.
        current_week: int
            Week number of the program when the operation took place.
        """
        query_investor = Query().id == investor_id
        investor = self.investors.get(query_investor)
        investor['parent'] = member_id
        investor['money'] = 0
        investor['week_joined'] = current_week
        investor['active'] = True
        investor['recruited'] = []
        self.members.insert(investor)
        self.investors.remove(query_investor)
        query_member = Query().id == member_id
        member = self.members.get(query_member)
        member['recruited'].append(investor_id)
        # since the new member pays 500 and the member that invited the investor gets 100, then the mummy gets 400
        member['money'] += 100
        self.members.update(member, query_member)
        query_mummy = Query().id == 0
        mummy = self.members.get(query_mummy)
        mummy['money'] += 400
        self.members.update(mummy, query_mummy)
    def get_members(self) -> list:
        """
        Returns an array with the documents of all the members of the program and are not the mummy.
        """
        return self.members.all()
    def get_mummy_money(self) -> int:
        """
        Returns the current money earned by the mummy
        """
        return self.members.get(Query().id == 0)['money']
    def eliminate_member(self, member_id, week) -> None:
        """
        Removes a member from the program
        Parameters
        ----------
        member_id : int
            The id of the member that will be marked as inactive.
        week : int
            Week number of the program when the operation took place.
        """
        query_member = Query().id == member_id
        member = self.members.get(query_member)
        member['active'] = False
        member['week_eliminated'] = week
        self.members.update(member, query_member)

