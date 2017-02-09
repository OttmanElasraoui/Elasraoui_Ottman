number = int(input("Enter a number: "))
digits = 0
average = 0
def avDigits():
    global digits, average, number
    num = number
    while num > 0:
        digits += 1
        average += number % 10
        num /= 10
    average /= digits
avDigits()

print("The average of the digits in ", number , "is", average)




