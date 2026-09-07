"""Create variables for order_total, delivery_region, and discount_percent to represent a 
   Zomato order. Follow Python naming conventions and print a sentence using all three variables, 
   like 'Order from [region] totals ₹[order_total] with [discount_percent]% discount.' """

order_total = 800
delivery_region = "Vastral Road"
discount_percent = 5

print("Price of your order:", order_total)
print("Delivery area:", delivery_region)
print("discount on your order:", discount_percent) 
print("Order from", delivery_region,"total ₹", order_total, "with", discount_percent, "% discount")

