import csv
import re

def get_words(filename):
    with open(filename, "r") as file:
        contents = file.read()

    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()


def save_counts(counts):
    with open("counts.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True): writer.writerow([word, count])