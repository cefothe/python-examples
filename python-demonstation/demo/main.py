import random

computer_number= random.randint(0, 100)

while True:
    print("I am thinking of a number, can you guess what it is?")
    user_input = int(input())
    if user_input == computer_number:
        print("You will")
        break
    elif user_input > computer_number:
        print("Too high")
    else :
        print("Too low")