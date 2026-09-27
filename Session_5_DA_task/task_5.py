"""5.Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set 
   of IRCTC train classes ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or 
   tuple for each. Write one sentence explaining your choice for both."""

# Favorite genres → List
favorite_genres = ["Action", "Comedy", "Horror"]
# It is a list because users' favorite genres might change in the future.

# IRCTC train classes → Tuple
train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")
# A tuple has been used because these are a fixed set of train classes that do not need to be changed.