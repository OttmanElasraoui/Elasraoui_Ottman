class Car:
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    def setCustom(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires
def main():
    Paint = input("Enter pain color: ")
    Interior = input("Enter your interior color: ")
    Engine = input("Enter engine type: ")
    Tires = input("Enter your tire type: ")
    
    car1 = Car(Paint, Interior, Engine, Tires)
    
    print("Your car is ready... ")
    print("Paint: " + car1.getPaint())
    print("Interior: " + car1.getInterior())
    print("Engine: " + car1.getEngine())
    print("Tires: " + car1.getTires())
    
main()
    

    
       


        
        
    
