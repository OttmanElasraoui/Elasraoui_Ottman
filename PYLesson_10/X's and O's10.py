import random
XAndO = []
for i in range (0, 4):
    XAndO.append([])
    for j in range (0, 4):
        switch = random.randint(0, 1)
        if switch == 1:
            XAndO[i].append("X")
        else:
            XAndO[i].append("O")
            
for values in XAndO:
    output = ""
    for value in values:
        output += value + "\t"
    print(output)



        
    
    
