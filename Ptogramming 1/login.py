import student_credentials
#calls the ditionary where student and staff login details are saved

def check_student (username, password):
    #Checks to see if student login credentials are in database
    if username in student_credentials.student_username and password in student_credentials.student_password:
        return 1
    else:
        return 0


def check_staff (username, password):
    # Checks to see if staff login credentials are in database
    if username in staff_cred_database.keys() and password in staff_cred_database.values():
        return 1
    else:
        return 0
