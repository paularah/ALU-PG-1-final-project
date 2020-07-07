import sqlite3
import format

"""
creates a connection to the database, a cursor for working with the db
"""
connection = sqlite3.connect(':memory:')
cur_sor = connection.cursor()
"""
creating a table with the specified fields.
"""
cur_sor.execute("""CREATE TABLE students (
name text,
email text,
nationality text,
age integer,
major text,
year text,
student_id text
)""")


# creates a student's profile in the database
def create_profile(name: str, email: str, nationality: str, age: int, major: str, year: str, student_id: str) -> None:
    try:
        with connection:
            cur_sor.execute(
                'INSERT INTO students VALUES (:name, :email, :nationality, :age, :major, :year, :student_id)', {
                    'name': name,
                    'email': email,
                    'nationality': nationality,
                    'age': age,
                    'major': major,
                    'year': year,
                    'student_id': student_id
                })
    except sqlite3.ProgrammingError:
        raise ValueError


def find_profile_by_id(student_id: str) -> str:
    try:
        with connection:
            cur_sor.execute('SELECT * FROM students WHERE student_id=:student_id', {'student_id': student_id})
            formatted_student = format.format_student(cur_sor.fetchone())
        return formatted_student
    except sqlite3.ProgrammingError:
        raise ValueError


def find_email_by_id(student_id: str) -> str:
    try:
        with connection:
            cur_sor.execute('SELECT * FROM students WHERE student_id=:student_id', {'student_id': student_id})
            email = cur_sor.fetchone()[1]
            return email
    except sqlite3.ProgrammingError:
        raise ValueError


def find_name_by_id(student_id: str) -> str:
    try:
        with connection:
            cur_sor.execute('SELECT * FROM students WHERE student_id=:student_id', {'student_id': student_id})
            name = cur_sor.fetchone()[0]
            return name
    except sqlite3.ProgrammingError:
        raise ValueError


def update_major(student_id: str, new_major: str) -> None:
    try:
        with connection:
            cur_sor.execute("""UPDATE students SET major = :new_major WHERE student_id = :student_id""",
                            {'new_major': new_major, 'student_id': student_id})
    except sqlite3.ProgrammingError:
        raise ValueError


def is_valid_email(email: str) -> bool:
    try:
        with connection:
            cur_sor.execute('SELECT * FROM students WHERE email=:email', {'email': email})
            if not cur_sor.fetchone():
                return False
            return True
    except sqlite3.ProgrammingError:
        raise ValueError
#
# create_profile('Paul', 'Arah', 23, 'Nigerian', 'Computer Science', '2nd', '233ehjdhe')
# create_profile('Ahmed', 'ahmed.com', 23, 'Nigerian', 'Computer Science', '2nd', 'eyjdehjdhe')
# print(is_valid_email('Arah'))


# print(send_message('233ehjdhe', 'ahmed.com', 'Hi THERE', 'student'))
