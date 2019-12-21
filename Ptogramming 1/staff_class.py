from parent_class import info
#imports the info model from parents class

class Staff(info):
    def __init__(self, name, age, nationality, faculty, contract):
        try:
            self.faculty = str(faculty)
            self.contract = str(contract)
            # invoking the __init__ of the info parent class
            info.__init__(self, name, age, nationality)
        except ValueError:
            print("A right values for")

    def show_info(self):
        # A method overiding the parent method to show a staff info
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("Nationality: " + self.nationality)
        print("Faculty: " + self.faculty)
        print("Contract: " + self.contract)