import unittest
from util import get_random_number, get_random_attributes, get_random_ids
from scipy.stats import kurtosis, skew

class TestUtil(unittest.TestCase):
    def test_get_random_number(self):
        result = get_random_number()
        self.assertTrue(result < 1)
        self.assertTrue(result > 0)
    def test_get_random_attributes(self):
        size = 100000 # large sample to get kurtosis and skewness
        normal = get_random_attributes('normal', size)
        for x in normal:
            kur = kurtosis(x)
            self.assertTrue(kur < 0.1)
            self.assertTrue(kur > -0.1)
        uniform = get_random_attributes('uniform', size)
        for x in uniform:            
            skewness = skew(x)
            self.assertTrue(skewness < 0.1)
            self.assertTrue(skewness > -0.1)
    def test_get_random_ids(self):
        size = 20
        ids = get_random_ids(size)
        self.assertTrue(len(ids) == len(set(ids)))
if __name__ == '__main__':
    unittest.main()