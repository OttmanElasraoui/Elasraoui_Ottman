word = input("Please enter a word: ")

def printTri():
    for i in range(0, len(word)):
        print(word[0:i])
printTri()
