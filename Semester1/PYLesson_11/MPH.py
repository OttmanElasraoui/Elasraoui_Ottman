class MilesPerHour:
    def __init__(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        mph = 0
    def setValues(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        mph = 0
    def GetDist(self):
        return self.distance
    def GetHours(self):
        return self.hours
    def GetMins(self):
        return self.minutes

    def getMPH(self):
        return self.distance/(self.hours + self.minutes / 60.0)
    
def main():
    distance = int(input("Enter The ditance: "))
    hours = int(input("Enter The hours: "))
    minutes = int(input("Enter The minutes: "))
    MPH = MilesPerHour(distance, hours, minutes)
    print(MPH.GetDist(), "in", MPH.GetHours(), "and", MPH.GetMins(), "minutes is", MPH.getMPH())
main()
    
    
    
        
        
        

    
    
    
