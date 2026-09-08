"""Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'],
   convert all to floats and calculate the total cart value."""

list = ['199.99', '299.50', '150']
total = float(list[0]) + float(list[1]) + float(list[2])
print("Total Cart Value: ", total)