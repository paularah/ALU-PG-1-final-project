"""
A Parent class that represnts an individual
@Author: Paul Arah
"""


class Info:
    # A parent class for info common to all child classes
    def __init__(self, first_name: str, last_name: str, age: int, nationality: str) -> object:
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.age = int(age)
        self.nationality = str(nationality)

    def show_info(self) -> None:
        # displays all the info for a particular person
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Nationality: " + str(self.nationality))
        pass
