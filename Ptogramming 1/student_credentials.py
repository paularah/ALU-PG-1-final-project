# a functinality for aappending to a dict modelling a database

class store_student_info(dict):
     # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value
    def add(self, key, value):
        self[key] = value

    # Main Function

student_cred_database = store_student_info()

def add_to_student_database(username, password):
    student_cred_database.add(username, password)
    pass

student_username = []
student_password = []

def add_to_student_login_list(username, password):
    student_username.append(username)
    student_password.append(password)
    pass

add_to_student_login_list(1,2)





