"""5.Suppose you have a list of messy 
   product names: [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']. Write code to clean each 
   name (remove spaces, replace hyphens with spaces, and make the brand title case) and print the 
   cleaned list.Constraint: Use at least three string methods from this session."""

products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_products = []

for product in products:
    clean_name = product.strip().replace("-", " ").title()
    cleaned_products.append(clean_name)

print(cleaned_products)