"""
This file holds the content and actions the user see when the are logged in
@Author : Paul Arah
"""

import time
from student_class import Student
import student_credentials
import staff_credentials
import message


def content_client(username: str, password: str, user_type: str) -> bool:
    while True:
        user_id = Student.create_id(username, password, user_type)
        time.sleep(1)
        print('Input a corresponding number to what you want to do')
        print('1. Show your Profile. ')
        print('2. Send A Message.')
        print('3. Check your Inbox.')
        print('4. See your Outbox.')
        print('5. Logout.')
        print('Input a corresponding number to what you want to do')
        print('')
        message_action = int(input('Input 1, 2, 3, 4 OR 5:   '))
        if message_action == 1:
            if user_type == 'student':
                print('_________________________________________________')
                print(student_credentials.find_profile_by_id(user_id))
                print('_________________________________________________')
            elif user_type == 'staff':
                print('_________________________________________________')
                print(staff_credentials.find_profile_by_id(user_id))
                print('_________________________________________________')
            else:
                raise ValueError
        elif message_action == 2:
            recipient = input('Input the Email Address of the recipient: ')
            print('Enter the recipient type')
            print('1. Student')
            print('2. Staff')
            recipient_type = int(input('Enter 1 OR 2: '))
            body = input('Type in your message here: ')
            if recipient_type == 1:
                recipient_type = 'student'
            elif recipient_type == 2:
                recipient_type ='staff'
            else:
                raise ValueError
            sender_type = user_type
            success: bool = message.send_message(user_id, recipient, body, recipient_type, sender_type)
            if success:
                print('Your message has been sent successfully!')
                print('__________________________________________________________________')
            else:
                print('Could not find a user with that email address')
                print('___________________________________________________________________')
        elif message_action == 3:
            inbox = message.check_inbox(user_id, user_type)
            print(inbox)
            print('________________________________________________________________________')
        elif message_action == 4:
            outbox = message.check_outbox(user_id, user_type)
            print('_________________________________________________________________________')
            print(outbox)
        elif message_action == 5:
            return True
        else:
            raise ValueError
