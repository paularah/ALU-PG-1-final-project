import unittest
from student_class import Student


class Test_Student(unittest.TestCase):
    # testing the student student class
    def test_student_instance(self):
        student_instance = Student('Paul', 'Arah', 23, 'Nigerian', 'Computer Science', '2nd')
        self.assertEqual(student_instance.first_name, 'Paul')
        self.assertEqual(student_instance.last_name, 'Arah')
        self.assertEqual(student_instance.age, 23)
        self.assertEqual(student_instance.nationality, 'Nigerian')
        self.assertEqual(student_instance.major, 'Computer Science')
        self.assertEqual(student_instance.year, '2nd')
        student_instance.save_student_profile('idddddddddd')

    # testing the decorator methods return the right properties
    def test_student_props(self):
        student_instance = Student('Paul', 'Arah', 23, 'Nigerian', 'Computer Science', '2nd')
        self.assertEqual(student_instance.fullname, 'Paul Arah')
        self.assertEqual(student_instance.email, 'p.arah@alustudent.com')

    # testing that the a create_id method returns the same id on the same input
    def test_unique_id(self):
        unique_id = Student.create_id('paul', 'arah', 'student')
        self.assertEqual(unique_id, Student.create_id('paul', 'arah', 'student'))


if __name__ == '__main__':
    unittest.main()
