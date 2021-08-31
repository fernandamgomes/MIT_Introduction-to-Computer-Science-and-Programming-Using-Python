'''
Write a program that uses bisection search to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year.

The following variables contain values as described below:
    - balance - the outstanding balance on the credit card
    - annualInterestRate - annual interest rate as a decimal
'''

monthly_interest_rate = annualInterestRate / 12
unpaid_balance = balance
lower_bound = balance/12
upper_bound =  (balance * (1 + monthly_interest_rate)**12) / 12.0 
guess = lower_bound

while unpaid_balance >= 0.01:
    for i in range(1, 13):
        interest = (unpaid_balance - guess)  * monthly_interest_rate
        unpaid_balance = unpaid_balance - guess  + interest
    unpaid_balance = round(unpaid_balance, 4)
    if unpaid_balance != 0:
        if unpaid_balance < 0.0:
            upper_bound = guess
        else:
            lower_bound = guess
        guess = (upper_bound + lower_bound) / 2
        unpaid_balance = balance

print("Lowest Payment:", round(guess, 2))
