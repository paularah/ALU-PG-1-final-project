"""
This is the interface of the ALU database the user interatcs with. It ia modelled to look
like some sort of frontend. The main code is held within an infinite loop to ensure the code
keeps running over and over again
"""

# catching all import errors before they occur
try:
    # importing all relevant files and classes
    import time
    from student_class import Student
    from staff_class import Staff
    import student_credentials
    import staff_credentials
    import login
    import create_profiles
except ImportError:
    print("Error importing files!")

while True:
    # keeps the entire apllication in an infinite loop
    print("Welcome to ALU database")
    print("Input a corresponding number that matches who your are")
    print("")
    print("1.  Student")
    print("2.  Staff")
    # Recieves a user input and cast to an integer before a assigning to user_type
    user_type = int(input("Input 1 for student, 2 for staff:  "))
    # conditions the user_type input for student
    if user_type == 1:
        print("Dear Student, welcome to the ALU database")
        print("")
        print("1. Sign up")
        print("2. Login")
        user_action = int(input("Choose a corresponding action: "))
        if user_action == 1:
            print("Create your login details")
            username = input("Username: ")
            password = input("Password: ")
            student_credentials.add_to_student_login_list(username, password)
            print("Your login credentials has been created! \n login next time with your username and password")
            time.sleep(2)
            print("Create Your Profile")
            create_profiles.create_student_profile()
            print("Your profile has been created and saved")



        elif user_action == 2:
            print("Input your login details")
            username = input("Username: ")
            password = input("Password:  ")
            check = login.check_student(username, password)
            if check == 1:
                Student.show_info()
            else:
                print("Incorrect Username or Password!")
        else:
            print("Choose an option!")
    elif user_type == 2:
        print("1. Sign up")
        print("2. Login")

        user_action = int(input("Choose a number corresponding to an option"))

        if user_action == 1:
            print("Create your login details")
            username = input("Username: ")
            password = input("Password: ")
            staff_credentials.add_to_staff_database(username, password)
            print("Your login credentials has been created")
        elif user_action == 2:
            print("Input your login details")
            username = input("Username: ")
            password = int("Password")
            check = staff_credentials.check_staff(username, password)
            if check == 1:
                Staff.show_info()
            else:
                print("Incorrect username or passowrd")
        else:
            print("Choose a valid option")
    else:
        print("Choose a valid option")
