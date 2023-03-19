'''
Author: Andrew Lounsbury
Date: 3/1/23
Purpose: prime number guessing game
'''
import math
import random

def prime(n):
    if n == 1:
        return False
    
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

Max = input("Enter a maximum number to set the difficulty: ")
while not Max.isdigit():
    Max = input("The maximum must be a positive integer: ")
Max = int(Max)

correct_guesses = 0
incorrect_guesses = 0
played_before = []

while True:
    
    random_number = random.randrange(1, Max)
    while random_number in played_before:
        random_number = random.randrange(1, Max)
    guess = input("Is " + str(random_number) + " prime (p) or composite (c)? Press q to quit ").lower()
    
    while guess != "p" and guess != "c" and guess != "q":
        print("Invalid input")
        guess = input("Is " + str(random_number) + " prime (p) or composite (c)? Press q to quit ").lower()
    
    if guess == "q":
        break
    if guess == "p" and prime(random_number) or guess == "c" and not prime(random_number):
        print("You got it right!")
        correct_guesses += 1
        played_before.append(random_number)
        Max += 5
    else:
        print("You got it wrong!")
        incorrect_guesses += 1

print("You got " + str(correct_guesses) + " correct and " + str(incorrect_guesses) + " incorrect! ")