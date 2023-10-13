#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

username = input("Enter username = ")
password = input("Enter password = ")
if username in users:
    index = users.index(username)

    if password == passwords[index]:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Access denied")
