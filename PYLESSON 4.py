print("(:*****^10)(:******^10)".format("test", "newtest"))

print("{:10.4f}".format(14443216.132165))

text = "yay!"
number = 847.465
print("*" * 20)
print("{:<10}{:10.2f}".format(text, number))
print("*" * 20)

def cube(side) :
        return(side**3)

side = int(input("16: "))

print("Your cube is ", cube(side), " cubic inces.")

def format (number) :
        output = "{:5.5f}".format(number)
        return output

num1 = 1 / 3
print(format(num1))

#global variable - available everwhere
var1 = "scope = everywhere in the program"

#/<---here is out of scope for var2
def mathod1():
        var2 = 47 # Scpoe for var2 is within method1()

def method2():# method2() is out of var2's scope
    var3 = 89.1

one = int(input("1"))
two = int(input("2"))

def add():
    print(one, " + " , two, " = ", add())

add(2)
display(2)



