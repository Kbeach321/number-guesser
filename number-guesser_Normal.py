
import random

attempts = 0
computer_number = random.randint(0, 3)

while attempts < 5:
    my_number =input("Guess A Number 1-100! ")
    attempts = attempts + 1
    my_number = int(my_number)

    if my_number < computer_number:
        print("Guess Number", attempts)
        print("Your number is too low")
    if my_number > computer_number:
        print("Guess Number", attempts)
        print("Your number is too high")
    if my_number == computer_number:
        print("YOU WON ON GUESS NUMBER", attempts)
        break
