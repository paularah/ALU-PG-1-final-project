class info():
    # A parent class for info common to all child classes
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def show_info(self):
        # dispays all the info for a particular person
        print("Name: " + str(self.name))
        print("Age" + str(self.age))
        print("Nationality" + str(self.nationality))


class Student(info):
    # A child class modelling student info
    info.__init__(self, name, age, nationality)
    def __init__(self, major, year):
        self.major = major
        self.year = year

    def show_info(self):
        # A method overiding the parent method to show a student info
        print("Name" + str(self.name))
        print("Age" + str(self.age))
        print("Nationality" + str(self.nationality))
        print("Major" + str(self.major))
        print("Year" + str(self.year))


class staff(info):
    def __init__(self, faculty, contract):
        self.faculty = faculty
        self.contract = contract

    def show_info(self):
        # A method overiding the parent method to show a staff info
        print("Name" + str(self.name))
        print("Age" + str(self.age))
        print("Nationality" + str(self.nationality))
        print("Faculty" + str(self.faculty))
        print("Contract " + str(self.contract))


Paul = Student("Paul", "age", "nationality", "IBT", "1")
print(Paul.name)
