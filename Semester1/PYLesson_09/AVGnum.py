import random
numbers = []
for i in range (0, 10):
    numbers.append(random.randint (1, 100))

print("Numbers... ")
output = ""
for number in numbers:
    output += str(number)+" "
print(output)
print("\n")
def average():
    av = 0
    for num in numbers:
        av += num
    return av/len(numbers)

print("The average of the above numbers is...", average())

