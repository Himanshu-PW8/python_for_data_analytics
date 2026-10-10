"""
1.Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying the discount. 
  Test it with price 1200 and discount_rate 0.15.   """


def calculate_final_price(price, discount_rate):
    discount = price * discount_rate
    final_price = price - discount
    return final_price

calculate_final_price(1200, 0.15)

