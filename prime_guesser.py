'''
Author: Andrew Lounsbury
Date: 1/3/23
Purpose: prime number guessing game
'''
import math
import random

def prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

Max = input("Enter a maximum number: ")
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
    guess = input("Is " + str(random_number) + " prime or composite? Press q to quit ").lower()
    
    if guess == "q":
        break
    if guess == "prime" and prime(random_number) or guess == "composite" and not prime(random_number):
        print("You got it right!")
        correct_guesses += 1
        played_before.append(random_number)
        Max += 5
    else:
        print("You got it wrong!")
        incorrect_guesses += 1

print("You got " + str(correct_guesses) + " correct and " + str(incorrect_guesses) + " incorrect! ")