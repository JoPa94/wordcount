def wordcount(happy):
    """
    Splits the input string and performs a frequency word check
    """

    words = happy.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print("The word frequency of your statement is: ")
    print(counts)

def main():
    happy = input("Enter a statement to word count: ")
    wordcount(happy)
main()
