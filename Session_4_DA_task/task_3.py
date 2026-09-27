"""3.Given the string 'Apple iPhone 14 Pro Max', use string slicing to extract and print only the 
     brand name and the model (i.e., 'Apple' and 'iPhone 14 Pro Max') separately.
     Hint:Use split() to help find the split point, then use slicing for the substrings."""

product = "Apple iPhone 14 Pro Max"

parts = product.split(" ", 1)

brand = parts[0]
model = parts[1]

print("Brand:", brand)
print("Model:", model)