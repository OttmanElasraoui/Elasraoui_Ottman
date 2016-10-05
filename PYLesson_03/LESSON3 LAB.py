class GetSs:
   def __init__(self, chk):
       self.check = chk
       self.count = 0


   def setCheck(self, chk):
       self.check = chk
       self.count = 0


   def countSs(self):
       for i in range(0, len(self.check)):
           if self.check[i] == "s":
               self.count += 1


   def __str__(self):
       self.countSs()
       return "The String " + self.check + " contains " + str(self.count) + " ss."


 Runner




from GetSs import*

def main():
   check = input("Please enter a String: ")
   s = GetSs(check)
   print(s)

   check = input("Please enter another String: ")
   s.setCheck(check)
   print(s)


main()

Output:
Please enter a String: 
sands
The String sands contains 2 ss.
Please enter another String: 
sisters
The String sisters contains 3 ss.
