Item1 = input("Enter your first item")
Price1 = int(input("Enter the price of your first item"))
Item2 = input("Enter your second item")
Price2 = int(input("Enter the price of your second item"))
Item3 = input("Enter your third item")
Price3 = int(input("Enter the priceof your third item"))
def printFormat(Item, Price):
    print("* {:<10}........{:10.2f}".format(Item, Price))

print("<<<<<<<<<<<<<<<___Recipt___>>>>>>>>>>>>>>>")
#line1
printFormat(Item1, Price1)
#line2
printFormat(Item2, Price2)
#line3
printFormat(Item3, Price3)

subtotal = Price1 + Price2 + Price3
tax = subtotal * 0.08
total = tax + subtotal

printFormat("Subtotal: ", subtotal)
printFormat("Tax: ", tax)
printFormat("Total: ", total)
print("__________________________________________")
print(" * Thank you for your support *")
 
