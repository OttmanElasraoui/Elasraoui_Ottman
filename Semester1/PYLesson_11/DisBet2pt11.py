import math
class Distance:
    def __init__(self, x1, x2, y1, y2):
        self.xone = x1
        self.xtwo = x2
        self.yone = y1
        self.ytwo = y2
        self.distance = 0
    def setValues(self, x1, x2, y1, y2):
        self.xone = x1
        self.xtwo = x2
        self.yone = y1
        self.ytwo = y2
        self.distance = 0
    def getDist(self):
        self.distance = math.sqrt((self.xtwo-self.xone)*(self.xtwo-self.xone)+(self.ytwo-self.yone)*(self.ytwo-self.yone))
        return self.distance
def main():
    x1 = int(input("Enter value for x1: "))
    x2 = int(input("Enter value for x2: "))
    y1 = int(input("Enter value for y1: "))
    y2 = int(input("Entervalue for y2: "))
    DIST = Distance(x1, x2, y1, y2)
    print(DIST.getDist())
main()
                 

            
                  
            
        
