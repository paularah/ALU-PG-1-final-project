"""
This file holds all the functions that format the results from the database into nicer
and readable formats
@Author: Paul Arah
"""


def format_student(student_input: tuple) -> str:
    try:
        student_result = 'Name:         {} \nEmail:        {}\nAge:          {} \nNationality:  {}  \nMajor:        {' \
                         '}  ' \
                         '\nYear:         {} '.format(
            student_input[0], student_input[1], student_input[2], student_input[3], student_input[4],
            student_input[5])
        return student_result
    except TypeError:
        raise ValueError


def format_staff(staff_input: tuple) -> str:
    try:
        staff_result = 'Name:         {}\nEmail:        {}\nAge:          {} \nNationality:  {}  \nFaculty:      {}  ' \
                       '\nContract:     ' \
                       '{} '.format(
            staff_input[0], staff_input[1], staff_input[2], staff_input[3], staff_input[4],
            staff_input[5])
        return staff_result
    except TypeError:
        raise ValueError


def format_inbox(name: str, messages: list, message_count: int) -> str:
    try:
        formatted_message = ''
        for i in messages:
            sender = i[1]
            formatted_message += '______________________________________________________________________________\n' \
                                 'Time Recieved: {}    Sender: {} \nBody: {}'.format(
                i[3], i[1], i[0])
        inbox_content = 'Dear {}, You have {} new messages!\n {}'.format(name, message_count, formatted_message)
        return inbox_content
    except TypeError:
        raise ValueError


def format_outbox(messages: list) -> str:
    try:
        if len(messages) == 0:
            return '______________________________________________________________\n No messages sent!'
        formatted_message = ''
        for i in messages:
            formatted_message += '______________________________________________________________________________\nTO: {' \
                                 '}\n{}'.format(i[2], i[0])
        return formatted_message
    except TypeError:
        raise ValueError
