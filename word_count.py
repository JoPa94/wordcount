happy = input("Enter a statement to check word frequency: ")

words = happy.split()#Split words at spaces

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
    
print("The word frequency of your statement is: ")
print(counts)
