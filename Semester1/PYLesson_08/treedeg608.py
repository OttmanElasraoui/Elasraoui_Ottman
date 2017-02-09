word = input("Enter a word: ")
stop = len(word)
def tree(word, start, stop):
    if start <= stop:
        print("{:>10s}".format(word[0:start]))
        start += 1
        tree(word, start, stop)
    
tree(word, 0, stop)    
    

