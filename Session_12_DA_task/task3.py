"""
3.Use filter() and a lambda function to extract only those Flipkart product names from a list that 
start with the letter 'S' (case-insensitive).   """


products = [
    'Samsung Phone',
    'iPhone',
    'Shoes',
    'Smart Watch',
    'Laptop',
    'speaker'
]

result = list(filter(lambda product: product.lower().startswith('s'), products))

print(result)
