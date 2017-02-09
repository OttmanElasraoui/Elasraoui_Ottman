import random

target = input("Enter your target: ")
enemyLoc = random.randint(1, 100)

if target == enemyLoc:
    print("It's a hit!")

else:
    print("Keep Trying!")
