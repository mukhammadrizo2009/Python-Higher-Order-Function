from pprint import pprint
prices = ["$120", "$340", "$50", "$90"]

result = [price.replace('$', " ") for price in prices]

pprint(result)