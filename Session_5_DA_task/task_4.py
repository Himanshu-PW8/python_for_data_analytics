"""4.Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second 
   filter and observe what error you get. Explain in a comment why this happens.
   Hint: Tuples are immutable, so direct assignment won't work."""

insta_filters = ("Clarendon", "Juno", "Lark", "Valencia")

# Try to update the second filter
insta_filters[1] = "Gingham"

# Error: TypeError
# Tuples are immutable, so their elements cannot be changed directly.