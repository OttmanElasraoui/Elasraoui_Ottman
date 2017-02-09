class Human:
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s
    def setMan(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s
    def getHair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getSkin(self):
        return self.skin
def main():
    h = input("Please enter hair color: ")
    e = input("Please enter eye color: ")
    s = input("Please enter skin color: ")

    MAN = Human(h, e, s)

    print("My info... ")
    
    print("Hair: " + MAN.getHair())
    print("Eyes: " + MAN.getEyes())
    print("Skin: " + MAN.getSkin())
main()
