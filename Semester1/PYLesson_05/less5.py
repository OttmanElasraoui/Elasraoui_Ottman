
def recursion():
    choice = input("would you like to do some recursion? ")
    if choice == "Y" or choice == "N":
        if choice == "Y":
            print("Lets do something")
        else:
            print("Spoiled the fun")

    else:
        print("Please enter Y or N")
        recursion()

recursion()
        
