try:
    import sqlite3
    import time
    import student_credentials
    import staff_credentials
    import format
except ImportError:
    print('Error importing, trying again')
    import sqlite3
    import time
    import student_credentials
    import staff_credentials
    import format

"""
This file is responsible for handling everything related to sending and recieving message
@Author: Paul Arah
"""

connection = sqlite3.connect(':memory:')
cur_sor = connection.cursor()

cur_sor.execute("""CREATE TABLE messages (
body text,
sender text,
recipient text,
timestamp text )""")


# sends a message
def send_message(user_id: str, recipient: str, body: str, recipient_type: str, sender_type: str) -> bool:

    if recipient_type == 'student':
        valid_email = student_credentials.is_valid_email(recipient)
        if not valid_email:
            return False
    elif recipient_type == 'staff':
        valid_email = staff_credentials.is_valid_email(recipient)
        if not valid_email:
            return False

    else:
        raise ValueError
    if sender_type == 'student':
        sender = student_credentials.find_email_by_id(user_id)
    elif sender_type == 'staff':
        sender = staff_credentials.find_email_by_id(user_id)
    else:
        raise ValueError
    timestamp = time.ctime()
    cur_sor.execute('INSERT INTO messages VALUES (:body, :sender, :recipient, :timestamp)', {
        'body': body,
        'sender': sender,
        'recipient': recipient,
        'timestamp': timestamp
    })
    return True


# checks inbox for new messages
def check_inbox(user_id: str, user_type: str) -> str:
    if user_type == 'student':
        recipient = student_credentials.find_email_by_id(user_id)
        name = student_credentials.find_name_by_id(user_id)
    elif user_type == 'staff':
        recipient = staff_credentials.find_email_by_id(user_id)
        name = staff_credentials.find_name_by_id(user_id)
    else:
        print(user_type)
        raise ValueError
    cur_sor.execute('SELECT * FROM messages WHERE recipient=:recipient', {'recipient': recipient})
    messages = cur_sor.fetchall()
    message_count = len(messages)
    inbox = format.format_inbox(name, messages, message_count)
    return inbox


# checks outbox for sent messages
def check_outbox(user_id: str, user_type: str) -> str:
    if user_type == 'student':
        sender = student_credentials.find_email_by_id(user_id)
    elif user_type == 'staff':
        sender = staff_credentials.find_email_by_id(user_id)
    else:
        raise ValueError
    cur_sor.execute('SELECT * FROM messages WHERE sender=:sender', {'sender': sender})
    messages = cur_sor.fetchall()
    outbox = format.format_outbox(messages)
    return outbox


