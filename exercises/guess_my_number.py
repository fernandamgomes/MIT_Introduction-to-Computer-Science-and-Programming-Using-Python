'''
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
'''

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = 50

while 0 <= guess <100:
    print("Is your secret number %d? " % guess)
    users_input = input( "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if users_input == "h":
        high = guess
        guess = (high + low) // 2
    elif users_input == "l":
        low = guess
        guess = (high + low) // 2
    elif users_input == "c":
        print("Game over. Your secret number was: %d" % guess)
        break
    elif users_input not in "chl":
        print("Sorry, I did not understand your input.")
