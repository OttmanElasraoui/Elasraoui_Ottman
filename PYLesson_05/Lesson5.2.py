def calcDisc(sub):
    if sub >= 2000:
        return sub*0.15

def printFormat(item, price):
    print("* {:<10}........{:10.2f}".format(item, price))

item1 = input("enter your first item")
price1 = int(input("enter price of your first item"))
item2 = input("enter your second item")
price2 = int(input("enter the price of your second item"))
item3 = input("enter your third item")
price3 = int(input("enter the price of your third item"))
item4 = input("enter your fourth item")
price4 = int(input("enter the price of your fourth item"))

subtotal = price1 + price2 + price3 + price4
discount = calcDisc(subtotal)
Tax = subtotal*.08
Total = subtotal - discount + Tax

print("<<<<<<<<<<< Receipt >>>>>>>>>>>")
#line1
printFormat(item1, price1)
#line2
printFormat(item2, price2)
#line3
printFormat(item3, price3)
#line4
printFormat(item4, price4)

printFormat("Subtotal: ", subtotal)
printFormat("Discount: ", discount)
printFormat("Tax: ", Tax)
printFormat("Total: ", Total)
print("_______________________________")
print("Thankyou for your support")



