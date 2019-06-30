class Investor:
    """
    Class representing an investor from the population of potentials members of the program
    """
    def __init__(self, investor_doc):
        self.innocence = investor_doc['innocence']
        self.experience = investor_doc['experience']
        self.charisma = investor_doc['charisma']
        self.id = investor_doc['id']
    def get_accept_probability(self) -> float:
        """
        Returns the probability of the investor accepting to join the program.
        """
        return self.innocence * (1 - self.experience)
