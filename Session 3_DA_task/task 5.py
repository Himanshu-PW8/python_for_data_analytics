"""5.You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. 
Use type casting to convert these to floats, then find and print the highest rating.
Hint:Use the float() function inside a loop or list comprehension."""

ratings = ['4.5', '3.0', '5', '4.2']
ratings = [float(rating) for rating in ratings]
print("Highest rating:", max(ratings))