# a functinality for aappending to a dict modelling a database
class store_staff_info(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value
    def add(self, key, value):
        self[key] = value

    # Main Function

staff_cred_database = store_staff_info()

def add_to_staff_database(username, password):
    staff_cred_database.add(username, password)
    pass