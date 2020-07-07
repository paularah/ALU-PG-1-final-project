try:
    from parent_class import Info
    import staff_credentials
except ImportError:
    print('Error importing, trying again')
    from parent_class import Info
    import staff_credentials

"""
staff class and its associated properties
@Author : Paul Arah
"""


# Staff class inherits from the info class
class Staff(Info):
    def __init__(self, first_name, last_name, age, nationality, faculty, contract):
        try:
            self.faculty = str(faculty)
            self.contract = str(contract)
            # invoking the constructor  of the info parent class
            Info.__init__(self, first_name, last_name, age, nationality)
        except ValueError:
            print("A right values for")

    # decorator to generate email
    @property
    def email(self):
        return '{}.{}@alueducation.com'.format(self.first_name[0].lower(), self.last_name.lower())

    # fullname to generate full from first and lastr name
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # saves a staff profile to the database
    def save_staff_profile(self, staff_id):
        staff_credentials.create_profile(self.fullname, self.email, self.nationality, self.age, self.faculty, self.contract, staff_id)

    # prints out the details of s staff
    def show_info(self):
        # A method overriding the parent method to show a staff info
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Nationality: " + self.nationality)
        print("Faculty: " + self.faculty)
        print("Contract: " + self.contract)
