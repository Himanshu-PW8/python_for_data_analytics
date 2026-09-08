"""2.Write a Python program that takes a user's input for the price of a Zomato order as a string, 
   converts it to a float using type casting, adds 18% GST, and prints the final bill amount."""

Order_price = input("Enter the Price of your Order: ")
Order_price = float(Order_price)
gst = Order_price * 18 / 100
final_bill = Order_price + gst
print("final_bill_amount: ", final_bill)