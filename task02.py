nums = [1, 2, 3, 4, 5]

def multiply(n):
    result = n ** 2
    return result

result = map(multiply, nums)
print(list(result))