L = int(input("What is the Length of your rectangle?"))
W = int(input("What is the Width of your rectamgle?"))
P = 0
def calcPerim():
    global perim
    perim = L*2 + W*2

calcPerim()
print("Your rectangle is,",perim,"ft around.")
