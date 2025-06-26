numbers = [18, 29, 3, 45, 7, 12]

result_min = min(numbers ,key=lambda x: x)
result_max = max(numbers ,key=lambda x: x)

print(f"Eng kichik son {result_min}!")
print(f"Eng katta son {result_max}!")