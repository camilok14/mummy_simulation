import unittest
from model.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        member_doc = {
            'id':123,
            'innocence': 0.1,
            'experience': 0.5,
            'charisma': 0.2,
            'recruited':[],
            'money': 1000,
            'week_joined': 3
        }
        self.member = Member(member_doc)
    def test_get_max_weeks(self):
        result = self.member.get_max_weeks()
        self.assertEqual(result, 4)
    def test_get_recruit_probability_with_recruit(self):
        for i in range(1, 11):
            self.member.recruited.append(i)
        result = self.member.get_recruit_probability()
        self.assertEqual(result, 0)
    def test_get_recruit_probability(self):
        result = self.member.get_recruit_probability()
        self.assertEqual(result, 0.1)
if __name__ == '__main__':
    unittest.main()