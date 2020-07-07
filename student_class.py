try:
    from parent_class import Info
    import student_credentials
    import uuid
except ImportError:
    print('Error Importing file, trying again')
    from parent_class import Info
    import student_credentials
    import uuid

"""
class modeling the details for a student 
@Author: Paul Arah
"""


# inherits from the info class
class Student(Info):
    # A child class modelling student info
    def __init__(self, first_name: str, last_name: str, age: int, nationality: str, major: str, year: str) -> object:
        self.major = str(major)
        self.year = str(year)
        # invoking the constructor of the info parent class
        Info.__init__(self, first_name, last_name, age, nationality)

    @property
    def fullname(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def email(self) -> str:
        return '{}.{}@alustudent.com'.format(self.first_name[0].lower(), self.last_name.lower())

    # creates a consistent unique id from the user name password and user type
    @staticmethod
    def create_id(username: str, password: str, user_tye: str) -> str:
        combine: str = username + password + user_tye
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, combine))

    # saves a student details to the database
    def save_student_profile(self, student_id: str) -> None:
        student_credentials.create_profile(self.fullname, self.email, self.nationality, self.age, self.major, self.year,
                                           student_id)

    # shows the info of a student
    def show_info(self) -> None:
        # A method overriding the parent method to show a student info
        print("Name: " + str(self.fullname))
        print('Email:   ' + str(self.email))
        print("Age: " + str(self.age))
        print("Nationality: " + str(self.nationality))
        print("Major: " + str(self.major))
        print("Year: " + str(self.year))
        pass

    """
    combines the username, password and user_type to generate a unique ID for  a user
    @:parameter username:string, password:string, user_type:string
    @:returns UUID:string 
    """
