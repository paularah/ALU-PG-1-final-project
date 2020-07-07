import unittest
from parent_class import Info


class TestParent(unittest.TestCase):

    def test_parent_instance(self):
        parent_instance = Info('paul', 'arah', 23, 'Nigerian')
        self.assertEqual(parent_instance.first_name, 'paul')
        self.assertEqual(parent_instance.last_name, 'arah')
        self.assertEqual(parent_instance.age, 23)
        self.assertEqual(parent_instance.nationality, 'Nigerian')


if __name__ == '__main__':
    unittest.main()
