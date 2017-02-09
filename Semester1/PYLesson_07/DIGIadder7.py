number = int(input("Please enter a number: "))
Sum = 0

def sumDigits():
    global Sum
    num = number
    while num > 0:
        Sum += 1
        num = int(num / 10)
sumDigits()
print("There are ", Sum, "digits in", number)
