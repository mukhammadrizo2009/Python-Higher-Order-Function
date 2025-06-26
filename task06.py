emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

result = list(filter(lambda emails: emails.endswith("@gmail.com"), emails))

print(result)