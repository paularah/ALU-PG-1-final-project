import sqlite3

"""
establishes a connection to the user database and creates a
table with specified fields
"""

connection = sqlite3.connect(':memory:')
cur_sor = connection.cursor()
cur_sor.execute("""CREATE TABLE users (
username text, 
password text,
user_type text  
)""")


# creates a new user
def create_user(username: str, password: str, user_type: str) -> None:
    with connection:
        cur_sor.execute('INSERT INTO users VALUES (:username, :password, :user_type)',
                        {'username': username, 'password': password, 'user_type': user_type})


# finds an existing user
def find_user(username: str, password: str, user_type: str) -> tuple:
    cur_sor.execute("SELECT * FROM users WHERE username=:username AND password=:password AND user_type=:user_type",
                    {'username': username, 'password': password, 'user_type': user_type})
    return cur_sor.fetchone()


# updates the username of a user
def update_username(username: str, password: str, new_username: str) -> None:
    with connection:
        cur_sor.execute(
            """UPDATE users SET username = :new_username WHERE username = :username AND password = :password""",
            {'username': username, 'password': password, 'new_username': new_username})


# updates the password of a user
def update_password(username: str, password: str, new_password: str) -> None:
    with connection:
        cur_sor.execute(
            """UPDATE users SET password = :new_password WHERE username = :username AND password = :password""",
            {'username': username, 'password': password, 'new_password': new_password})
    print(cur_sor.fetchall())


