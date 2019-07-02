from time import sleep
from model.member import Member
from model.investor import Investor
from controller.db import DatabaseController
from controller.log import Logger
from util import get_random_attributes, get_random_ids, get_random_number

allowed_distributions = ['uniform', 'normal']
class Simulation:
    """
    The main class to manage the simulation of the  of the Mummy Money, Get Rich Quick Program!.
    Allows to setup the simulation parameters and start the simulation.
    """
    def __init__(self, population, timelapse, distribution):
        """ Simulation: int, int, string -> None
            Creates an instance of the Simulation
            Parameters
            ----------
            population : int
                Number of investors in the simulation universe.
            timelapse : int
                Number of seconds the software will take to simulate a week's membership.
            distribution : string
                Can only take the values 'uniform' or 'normal'
                Distribution used to generate the innocence, experience and charisma attributes
                of the investors.        
        """
        if distribution not in allowed_distributions:
            raise ValueError('Allowed values for distribution are: ' + ', '.join(allowed_distributions))
        self.logger = Logger()
        self.population = population
        self.timelapse = timelapse
        self.distribution = distribution
        self.db_controller = DatabaseController(True)
        self.continue_simulation = True
        self.__set_week__(0)
    def __set_week__(self, week):
        self.current_week = week
        self.db_controller.set_current_week(self.current_week)
        self.logger.log('Current week is {}'.format(week))
    def __create_investors_universe__(self) -> None:
        """
        Populates database with universe of investors, using the parameters given on the constructor of the simulation.
        """
        attributes = get_random_attributes(self.distribution, self.population)
        ids = get_random_ids(self.population)
        for i in range(self.population):
            investor_doc = {'id': ids[i], 'innocence': attributes[0, i], 'experience': attributes[1, i], 'charisma': attributes[2, i]}
            self.db_controller.add_investor(investor_doc)
            if ((i + 1) % 1000 == 0):
                self.logger.log('Created {} investors of {}'.format((i + 1), self.population))
    def __add_first_members__(self):
        """
        Adds the mummy as a member and invites the 10 first members from the universe of investors.
        """
        # The mummy invites itself to be a member
        self.db_controller.add_member(0, 0, self.current_week)
        # The mummy invites the first 10 members
        for _ in range(10):
            investor = self.db_controller.get_random_investor()
            self.db_controller.add_member(investor['id'], 0, self.current_week)
    def __simulate_one_week__(self):
        """
        Makes the program being simulated to advance in one week.
        This method will search all active members and apply the rules of the program.
        """
        self.__set_week__(self.current_week + 1)
        members = self.db_controller.get_members()
        filtered = filter(lambda x: (len(x['recruited']) < 10) & x['active'], members)
        members = list(filtered)
        if not members:
            self.continue_simulation = False
            return
        for member_doc in members:
            member = Member(member_doc)
            # 3.b of the document actually says "If the number is greater than the member's probability..."
            # I'm going to use "less than", to make sense. The bigger the probability, the more likely the statement to be true            
            if get_random_number() < member.get_recruit_probability():
                candidate = Investor(self.db_controller.get_random_investor())
                self.logger.log('Member {} will try to recruit investor {}'.format(member.id, candidate.id))
                # Same problem with 3.c of the document
                if get_random_number() < candidate.get_accept_probability():
                    self.logger.log('Investor {} will join the program invited by member {}'.format(candidate.id, member.id))
                    member.money += 100
                    self.db_controller.add_member(candidate.id, member.id, self.current_week)
                else:
                    self.logger.log('Investor {} will not join the program'.format(candidate.id))
            else:
                self.logger.log('Member {} will not recruit a new investor'.format(member.id))
            lasted_weeks = self.current_week - member.week_joined
            if (member.money < 500) & (lasted_weeks >= member.get_max_weeks()):
                self.logger.log('Member {} did not recover the investment in {} weeks and will be eliminated from the program with MM${}.'.format(member.id, lasted_weeks, member.money))
                self.db_controller.eliminate_member(member.id, self.current_week)

    def run(self):
        """
        Runs the simulation.
        The simulatiom will stop when there are no more active members.
        """
        self.__create_investors_universe__()
        self.__add_first_members__()
        while self.continue_simulation:
            sleep(self.timelapse)
            self.__simulate_one_week__()
        mummy_money = self.db_controller.get_mummy_money()
        self.logger.log('The program ended in {} weeks and the mummy got MM${}'.format(self.current_week, mummy_money))
