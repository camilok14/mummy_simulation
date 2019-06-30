from time import sleep
from model.member import Member
from model.investor import Investor
from controller.db import DatabaseController
from util import get_random_attributes, get_random_ids, get_random_number

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
        allowed_distributions = ['uniform', 'normal']
        if distribution not in allowed_distributions:
            raise ValueError('Allowed values for distribution are: ' + ', '.join(allowed_distributions))
        self.population = population
        self.timelapse = timelapse
        self.distribution = distribution
        self.db_controller = DatabaseController(True)
        self.current_week = 0
    
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
                print('Created {} investors of {}'.format((i + 1), self.population))