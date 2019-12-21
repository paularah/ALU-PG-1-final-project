from parent_class import info


class Student(info):
    # A child class modelling student info
    def __init__(self, name, age, nationality, major, year):
        try:
            self.major = str(major)
            self.year = str(year)
            # invoking the __init__ of the info parent class
            info.__init__(self, name, age, nationality)
        except ValueError:
            return None

    def show_info(self):
        # A method overiding the parent method to show a student info
        me =self
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Nationality: " + str(self.nationality))
        print("Major: " + str(self.major))
        print("Year: " + str(self.year))







