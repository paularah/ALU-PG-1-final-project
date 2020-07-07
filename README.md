# ALU Programming I Final Project 
##Project Description
This is a platform that brings together the staff and students in the ALU community.
The platform holds a database of students and staffs in the ALU community and also
makes it easy to communicate with each other. 

##Features
* Login: Users can log in with a username and a password
* Signup: Users can signup with a username and a password
* Create Profile: Users can create a profile of the data
* View Profile: Users can view their profiles
* Check Inbox: Logged in users can check their inbox
* Check Outbox: Logged in users can check their inbox
* Send Message: Logged in users send a message to other users
* Log out: users can log out of the platform. 


## How to use
This project does use any external dependencies, so no need to install anything.
Run the main_client.py file from your IDE or use the command below on the terminal.

```shell script
python main_client.py
```
Navigate to the root folder on of the app on your machine and run the command above.

## Test Suites


**Test Student class in student_class.py:**

Test Case| Description | Status 
------------ | ------------- | -------------
Test object instantiation | checks that the obejct is correctly instantiated | pass
email | test that the email decorator generates the right email depending on the type of user | pass
Fullname | test that the full name of a user is generated | pass
profile save | test that a student profile is saved to the database| pass
correct profile | test that the actual correct profile is what is in the database | pass
create ID | test that an a unique ID is created for a user | pass
same ID | test that same ID is generated on the same input | pass
show info | test the right info about a student is shown | pass



**Test Staff class in staff_class.py**

Test Case| Description | Status 
------------ | ------------- | -------------
Test object instantiation | checks that the obejct is correctly instantiated | pass
profile save | test that a staff profile is saved to the database| pass
show info | test the right info about a staff is shown | pass
Fullname | test that the full name of a staff is generated | pass
mail | test that the email decorator generates the right email depending on the type of user | pass



**Test User database  in user.py**

Test Case| Description | Status 
------------ | ------------- | -------------
create user| test that the create user function creates a user | pass
find user | test the the find user returns the right user based on the user id | pass
update username | test the a username is updated in the user database | pass
update password | test the a user's password is correctly updated | pass


**Test staff database  in staff_credential.py**

Test Case| Description | Status 
------------ | ------------- | -------------
create profile|  test that a staffs profile is inserted into the staff database | pass
find profile by id | test that a staff profile can be found using the unique ID | pass
find email  by id |  test that a the correct email is returned when a valid staff id is used | pass
is valid email | test that the email is a present the in the staff database | pass
