import unittest
import users


class TestUserDB(unittest.TestCase):

    def test_create_user(self):
        users.create_user('paul', 'arah', 'student')
        user = users.find_user('paul', 'arah', 'student')
        self.assertEqual(type(user), tuple)
        self.assertEqual(user, ('paul', 'arah', 'student'))

    def test_find_user(self):
        user = users.find_user('paul', 'arah', 'student')
        self.assertEqual(type(user), tuple)
        self.assertEqual(user, ('paul', 'arah', 'student'))

    def test_not_found(self):
        found = users.find_user('father', 'mars', 'goat')
        self.assertEqual(found, None)

    def test_username_update(self):
        users.update_username('paul', 'arah', 'samson')
        user = users.find_user('samson', 'arah', 'student')
        self.assertEqual(type(user), tuple)
        self.assertEqual(user, ('samson', 'arah', 'student'))

    def test_password_update(self):
        users.create_user('wens', 'arah', 'student')
        users.update_password('wens', 'arah', 'alu')
        user = users.find_user('wens', 'alu', 'student')

        self.assertEqual(type(user), tuple)
        self.assertEqual(user, ('wens', 'alu', 'student'))


if __name__ == '__main__':   
    unittest.main()
