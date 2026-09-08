"""3.Build a Python script that asks the user for their Zomato order total and prints 
     'Apply Free Delivery' if total is above 299, 'Add more items for free delivery' 
     if between 200 and 299, else 'Delivery charges apply'."""

Order = int(input("Enter your Total Zomato Order: "))
if Order > 299:
    print("It is free delivery")
elif Order > 200 and Order < 299:
    print("You can add more items for free delivery")
else :
    print("Delivery Charges will be applied to your order")