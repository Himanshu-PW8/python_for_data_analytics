"""4.Write a Python program using nested if statements: take a user's entered Flipkart cart value 
and payment method ('UPI', 'Card', 'Cash'). If the cart value is above 1000 and payment method 
is 'UPI', print 'Eligible for 10% cashback'; if above 1000 and payment is not 'UPI', print 
'Eligible for 5% cashback'; else print 'No cashback'."""

flipkart_cart_value = int(input("Enter your total cart value: "))
payment_method = input("Enter your payment method: ")

if flipkart_cart_value > 1000:
    if payment_method == "UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")