data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

words = filter(
    lambda item: type(item) == str and len(item) > 5,
    data
)

print(list(words))

