from numpy.random import normal, uniform
from random import sample, random
def get_random_attributes(dist, size) -> list:
    """
    Returns a list of 3 lists of size random numbers.
    Each one of the 3 lists will have a dist distribution.
    Parameters
    ----------
    dist : string
        If dist is 'normal' the 3 lists will have a normal distribution, otherwise the list will have a uniform distribution.
    size: int
        Length of the 3 lists with the random numbers.
    """
    if dist == 'normal':
        return normal(0.5, 0.1, (3, size))
    return uniform(0.0, 1.0, (3, size))
def get_random_ids(size) -> list:
    """
    Returns a list of int without duplicates and without 0, which is the mummy member id
    Parameters
    ----------
    size : int
        Length of the list to return.
    """
    return sample(range(1, size + 1), size)
def get_random_number() -> float:
    """
    Returns a random number between 0 and 1
    """
    return random()