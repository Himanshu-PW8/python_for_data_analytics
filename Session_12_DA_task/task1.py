"""
1.Write a lambda function that takes a price in rupees and returns the price after adding 18% GST. 
Test it on the prices 100, 250, and 500.    """


gst = lambda price: price + (price * 18 / 100)

print(gst(100))
print(gst(250))
print(gst(500))
