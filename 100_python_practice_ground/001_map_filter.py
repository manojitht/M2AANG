products = [
    ("butter", 25),
    ("cake", 18),
    ("chocolate", 63),
]

x = list(map(lambda product: product[1], products))
print(x)

x = list(filter(lambda product: product[1] > 20, products))
print(x)
