import random

def recursion():
    guess = int(input("Pick a number between 1 and 10"))
    number = random.randint(1, 10)
    if guess >= 1 and guess <= 10:
        if guess == number:
            print("the number is right!")
        else:
            print("WRONG!!")
    else:
        print("please make it 1-10")
        recursion()

recursion()
