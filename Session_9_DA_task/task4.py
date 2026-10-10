"""
4.Given a function apply_discount(price, rate=0.10), update it so that if the rate is not passed, it uses 0.10 by default. 
  Then, call it with only the price argument and print the result.Hint:Use default arguments in your function definition.   """


def apply_discount(price, rate=0.10):
    discount = price * rate
    return price - discount

print(apply_discount(1000))
