from collections import Counter

s = input("Enter a sentence to count words: ")

words = Counter(s.split(" "))
print(words)