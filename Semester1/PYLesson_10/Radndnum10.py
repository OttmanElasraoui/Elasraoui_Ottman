import random
numbersList = []

for i in range (0, 4):
    numbersList.append([])
    for j in range (0, 4):
        numbersList[i].append(random.randint(1, 100))
        
for numbers in numbersList:
   output = ""
   for number in numbers:
       output += str(number) + "\t"
   print(output)
