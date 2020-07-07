"""
@Author : Paul Arah
"""

try:
    import unittest
    from staff_class import Staff
    import staff_credentials
    import student_credentials
except ImportError:
    import unittest
    from staff_class import Staff
    import staff_credentials
    import student_credentials


class TestStaff(unittest.TestCase):

    def test_staff_instance(self):
        staff_instance = Staff('Paul', 'Arah', 23, 'Nigerian', 'Computer Science', 'full time')
        self.assertEqual(staff_instance.first_name, 'Paul')
        self.assertEqual(staff_instance.last_name, 'Arah')
        self.assertEqual(staff_instance.age, 23)
        self.assertEqual(staff_instance.nationality, 'Nigerian')
        self.assertEqual(staff_instance.faculty, 'Computer Science')
        self.assertEqual(staff_instance.contract, 'full time')

    def test_staff_props(self):
        staff_instance = Staff('Paul', 'Arah', 23, 'Nigerian', 'Computer Science', 'full time')
        self.assertEqual(staff_instance.fullname, 'Paul Arah')
        self.assertEqual(staff_instance.email, 'p.arah@alueducation.com')


if __name__ == '__main__':
    unittest.main()
