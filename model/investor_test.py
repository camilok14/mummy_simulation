import unittest
from model.investor import Investor

class TestInvestor(unittest.TestCase):
    def test_get_accept_probability(self):
        inverstor_doc = {'id':123, 'innocence': 0.1, 'experience': 0.5, 'charisma': 0.2}
        investor = Investor(inverstor_doc)
        result = investor.get_accept_probability()
        self.assertEqual(result, 0.05)
if __name__ == '__main__':
    unittest.main()