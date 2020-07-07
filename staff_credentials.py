try:
    import sqlite3
    import format
except ImportError:
    print('Error Importing, trying again')
    import sqlite3
    import format

"""
creates a connection to the database, a cursor for working with the db
@Author: Paul Arah
"""
connection = sqlite3.connect(':memory:')
cur_sor = connection.cursor()
"""
creating a table with the specified fields.
"""
cur_sor.execute("""CREATE TABLE staffs (
name text,
email text,
nationality text,
age integer,
faculty text,
contract text,
staff_id text
)""")


# creates a staff's profile in the database
def create_profile(name: str, email: str, nationality: str, age: int, faculty: str, contract: str, staff_id: str) -> None:
    with connection:
        cur_sor.execute('INSERT INTO staffs VALUES (:name, :email, :nationality, :age, :faculty, :contract, :staff_id)',
                        {
                            'name': name,
                            'email': email,
                            'nationality': nationality,
                            'age': age,
                            'faculty': faculty,
                            'contract': contract,
                            'staff_id': staff_id
                        })


# finds a profile by the id
def find_profile_by_id(staff_id: str) -> str:
    with connection:
        cur_sor.execute('SELECT * FROM staffs WHERE staff_id=:staff_id', {'staff_id': staff_id})
        formatted_staffs = format.format_staff(cur_sor.fetchone())
    return formatted_staffs


# finds a email by the ID
def find_email_by_id(staff_id: str) -> str:
    with connection:
        cur_sor.execute('SELECT * FROM staffs WHERE staff_id=:staff_id', {'staff_id': staff_id})
        email = cur_sor.fetchone()[1]
        return email


# finds the name of a by the id
def find_name_by_id(staff_id: str) -> str:
    with connection:
        cur_sor.execute('SELECT * FROM staffs WHERE staff_id=:staff_id', {'staff_id': staff_id})
        name = cur_sor.fetchone()[0]
        return name


# checks if the email is present in the database
def is_valid_email(email: str) -> bool:
    with connection:
        cur_sor.execute('SELECT * FROM staffs WHERE email=:email', {'email': email})
        if not cur_sor.fetchone():
            return False
        return True


# updates the faculty of a staff
def update_faculty(staff_id: str, new_faculty: str) -> None:
    with connection:
        cur_sor.execute("""UPDATE staffs SET faculty = :new_faculty WHERE staff_id = :staff_id""",
                        {'new_major': new_faculty, 'student_id': staff_id})
