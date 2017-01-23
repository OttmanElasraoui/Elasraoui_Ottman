words = ["dog", "cat", "sheep", "hen", "mouse"]
print("In order....")
for word in words:
    print(word)

print("\nReversed....")
def reverse():
    for i in range(len(words)-1, 0, -1):
        print(words[i])


reverse()
        


