H = int(input("Enter height"))
L = int(input("Enter length"))
W = int(input("Enter width"))
vol = 0
def calcVol():
    global vol
    vol = H * L * W
calcVol()
print("The volume is,", vol , "Correct?")

