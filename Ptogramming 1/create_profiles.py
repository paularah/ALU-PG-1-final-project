#Catching errors arising from importing files
try:
    from student_class import Student
    from staff_class import  Staff
except ImportError:
    print("Error importing!")

global_student_instance  = None

def create_student_profile():
        print("Please input the right information in the appropraite fields")
        student_name = input("Input your name: ")
        student_nationality = input("Input your nationality: ")
        student_age = input("Input your age: ")
        student_major = input("Input your major: ")
        student_year = input("Input your year: ")
        student_instance = Student(student_name, student_age, student_nationality, student_major, student_year)
        student_instance.show_info()
        return student_instance



check = create_student_profile()
check.show_info()





