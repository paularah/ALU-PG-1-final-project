"""
This is the interface of the ALU database the user interacts with. It ia modelled to look
like some sort of frontend. The main code is held within an infinite loop to ensure the code
keeps running over and over again
@Author : Paul Arah
"""

# catching all import errors before they occur
try:
    # importing all relevant files and classes
    import time
    from student_class import Student
    from staff_class import Staff
    import student_credentials
    import staff_credentials
    import users
    import message
    from content_client import content_client
except ImportError:
    print("Error importing files!")
    print('Trying again')
    import time
    from student_class import Student
    from staff_class import Staff
    import student_credentials
    import staff_credentials
    import users
    import message

while True:
    try:
        # keeps the entire application in an infinite loop
        print('')
        print("Welcome to ALU database")
        print("Input a corresponding number that matches who your are")
        print("")
        print("1.  Student")
        print("2.  Staff")
        # Receives a user input and cast to an integer before a assigning to user_type
        user_type = int(input("Input 1 for student, 2 for staff:  "))
        # conditions the user_type input for student
        if type(user_type) != int:
            raise ValueError
        if user_type == 1:
            print("Dear Student, welcome to the ALU database")
            print("")
            print("1. Sign up")
            print("2. Login")
            user_type = 'student'
            user_action = int(input("Choose a corresponding action: "))
            if type(user_action) != int:
                raise ValueError
            if user_action == 1:
                print("Sign up to the ALU community database")
                username = input("Username: ")
                password = input("Password: ")
                user_type = 'student'
                found = users.find_user(username, password, user_type)
                if found:
                    print('Error: A user with this details already exist! Log in instead.')
                    continue
                users.create_user(username, password, user_type)
                print("Your login credentials has been created! \nLogin next time with your username and password")
                time.sleep(2)
                print('______________________________________________________________________________')
                print('Now its time to create your profile. Please enter the relevant details below')
                first_name = str(input('Enter your first name: '))
                last_name = str(input('Enter your last name: '))
                age = int(input('Enter your age: '))
                nationality = str(input('Enter your nationality: '))
                major = str(input('Enter your major: '))
                year = str(input('Enter your year: '))
                student_id = Student.create_id(username, password, user_type)
                new_student = Student(first_name, last_name, age, nationality, major, year)
                new_student.save_student_profile(student_id)
                print("Your profile has been created and saved!")
                print('__________________________________________________________________________________')
                print("")
                while True:
                    state = content_client(username, password, user_type)
                    if state:
                        break

            elif user_action == 2:
                print("Input your login details")
                username = input("Username: ")
                password = input("Password:  ")
                user_type = 'student'
                found = users.find_user(username, password, user_type)
                if not found:
                    print('Error: Incorrect Username or Password!')
                    continue
                while True:
                    student_id = Student.create_id(username, password, user_type)
                    student_name = student_credentials.find_name_by_id(student_id)
                    print('Dear {}, Welcome back!'.format(student_name))
                    state = content_client(username, password, user_type)
                    if state:
                        break
            else:
                raise ValueError
        elif user_type == 2:
            print("Dear Staff, welcome to the ALU database")
            print("")
            print("1. Sign up")
            print("2. Login")
            user_type = 'staff'
            user_action = int(input("Choose a number corresponding to an option: "))
            if user_action == 1:
                print("Sign up to the ALU community database")
                username = input("Username: ")
                password = input("Password: ")
                user_type = 'staff'
                found = users.find_user(username, password, user_type)
                if found:
                    print('Error: A user with this details already exist! Log in instead.')
                    continue
                users.create_user(username, password, user_type)
                print("Your login credentials has been created! \nLogin next time with your username and password")
                print('______________________________________________________________________________')
                print('Now its time to create your profile. Please enter the relevant details below')
                first_name = str(input('Enter your first name: '))
                last_name = str(input('Enter your last name: '))
                age = int(input('Enter your age: '))
                nationality = str(input('Enter your nationality: '))
                faculty = str(input('Enter your faculty: '))
                contract = str(input('Enter your contract type: '))
                staff_id = Student.create_id(username, password, user_type)
                new_staff = Staff(first_name, last_name, age, nationality, faculty, contract)
                new_staff.save_staff_profile(staff_id)
                print("Your profile has been created and saved!")
                print('________________________________________________________________________________')
                while True:
                    state = content_client(username, password, user_type)
                    if state:
                        break
            elif user_action == 2:
                print('Input your login details')
                username = str(input("Username: "))
                password = str(input("Password: "))
                user_type = 'staff'
                found = users.find_user(username, password, user_type)
                if not found:
                    print('Error: Incorrect Username or Password!')
                    continue
                staff_id = Student.create_id(username, password, user_type)
                staff_name = staff_credentials.find_name_by_id(staff_id)
                print('Dear {}, Welcome back'.format(staff_name))
                while True:
                    state = content_client(username, password, user_type)
                    if state:
                        break
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError or TypeError:
        print('Invalid Input: Input must be Valid Number. Try again!')
