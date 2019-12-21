class info():
    # A parent class for info common to all child classes
    def __init__(self, name, age, nationality):
        self.name = str(name)
        self.age = str(age)
        self.nationality = str(nationality)

    def show_info(self):
        # dispays all the info for a particular person
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Nationality: " + str(self.nationality))
        pass

