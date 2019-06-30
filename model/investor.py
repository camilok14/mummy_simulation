class Investor:
    """
    Class representing an investor from the population of potentials members of the program
    """
    def __init__(self, investor_doc):
        """
        Parameters
        ----------
        investor_doc : dict
            Document with the attributes of the investor.
        """
        self.innocence = investor_doc['innocence']
        self.experience = investor_doc['experience']
        self.charisma = investor_doc['charisma']
        self.id = investor_doc['id']
    def get_accept_probability(self) -> float:
        """
        Returns the probability of the investor accepting to join the program.
        """
        # This formula gives a bigger probability when the investor is more innocent and has little experience
        not_experience = 1 - self.experience
        return self.innocence * not_experience
