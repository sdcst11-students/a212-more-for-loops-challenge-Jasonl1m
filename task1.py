#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
ans = 11
attempts = 0
for i in range(10):
    x = int(input("Enter a integer from 1 to 100 = "))
    if x == ans:
        print("The number is correct!")
        break
    elif x > ans:
        if i == 9:
            print("You have lost")
            break
        print("The number is too high")
    elif x < ans:
        if i == 9:
            print("You have lost")
            break
        print("The number is too low")