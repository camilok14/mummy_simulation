from math import log10, floor
from model.investor import Investor
class Member(Investor):
    """
    Class representing a member of the program. Inherits from Investor.
    """
    def __init__(self, member_doc):
        """
        Parameters
        ----------
        member_doc : dict
            Document with the attributes of the member.
        """
        Investor.__init__(self, member_doc)
        self.recruited = member_doc['recruited']
        self.money = member_doc['money']
        self.week_joined = member_doc['week_joined']
    def get_recruit_probability(self) -> float:
        """
        Returns the probability of the member finding an investor to join the program
        """
        x = len(self.recruited)
        # The document does not cover the case of a member that has not recruited anyone, since log10 cannot be evaluated on 0 I will force it to be 1.
        if x == 0:
            x = 1
        factor = 1 - log10(x)
        return self.experience * self.charisma * factor
    def get_max_weeks(self) -> int:
        """
        Returns the maximum number of weeks that the member can remain int he program without recovering their investment
        """
        not_innocence = 1 - self.innocence
        # Document uses a factor 10, but it would give numbers too small and members would not tolerate many weeks. I will use 50
        return floor(not_innocence * self.experience * self.charisma * 50)