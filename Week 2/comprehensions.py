#List and Dictionaries
from helpers import get_words, save_counts

def main():
    # counts = {}  #dictionary
    words = get_words("address.txt") #List of words
    lowercase_words = [word.lower() for word in words ]
    # lowercase_words = [word.lower() for word in words if  len(word) > 4]

    counts = {word: words.count(word) for word in lowercase_words }
    # for word in words:
    #     if word in counts:
    #         counts[word]+=1
    #     else:
    #         counts[word]=1

    save_counts(counts)

main()