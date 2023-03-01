
# Zainab Mahdi, Gianni Oquendo, Giovanni Lopez
# CSE 5408
# Group 4
# Spring 2023
# Lab 4

# Imports:
from datetime import datetime

# Part A: Output Reverse Input String - Gianni


# Part B: Check If Entered Number Is Prime - Zainab
num = int(input("input the number to check it "))
if (num <= 1):
    print("The number is not prime")
else:
    for i in range(2, num):
        if (num%i == 0): # If the number has a divisor
            print("The number is not prime")
            break
    else: # If the for loop ends without reaching any break
        print("The number is prime")


# Part C: Output Current Time In Military Time - Giovanni
current = datetime.now()
currenttime = current.strftime('%H%M')
print('Current Time Is: ', currenttime)