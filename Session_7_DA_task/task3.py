"""3.Build a Python script that asks the user for their Zomato order total and prints 
'Apply Free Delivery' if total is above 299, 'Add more items for free delivery' 
if between 200 and 299, else 'Delivery charges apply'."""

Total_Order = int(input("Enter your Total Price Of your order: "))
if Total_Order > 299:
    print("Apply Free Delivery")
elif Total_Order > 200:
    print("Add more items for free delivery")
else :
    print("Delivery charges apply")
