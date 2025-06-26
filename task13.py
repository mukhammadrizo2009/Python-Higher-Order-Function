sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()

result = sorted(words, key=lambda word: len(word), reverse=True)[:3]

print(result)
