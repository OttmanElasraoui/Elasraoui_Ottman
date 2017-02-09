sentence = input("Enter a string: ")
def replace():
    global sentence
    while sentence.count(" ") > 0:
        sentence = sentence[0 : sentence.index(" ")] +"_"+ sentence[sentence.index(" ")+1 : len(sentence)]
replace()
print(sentence)
                            
