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
