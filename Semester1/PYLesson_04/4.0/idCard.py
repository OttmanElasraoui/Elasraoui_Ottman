N = input("Enter your first name")
L = input("Enter your last name")
T = input("Enter your title")
S = input("Enter your school name")
Y = input("Enter the school year")
U = input("What is the subject")

print("*" * 24)

def printFormat(left, right):#prints a single line in the card
    print("* {:^10}{:^10} *".format(left, right))

#line1
printFormat(S, Y)
#line2
printFormat(N, L)
#line3
printFormat(T, U)
print("*" * 24)

