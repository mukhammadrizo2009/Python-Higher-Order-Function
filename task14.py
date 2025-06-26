from pprint import pprint
words = ["sun", "mountain", "a", "apple"]

words.sort(key=lambda word: len(word),reverse=True)

pprint(words)