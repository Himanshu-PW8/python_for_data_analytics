"""4.Given two sets: set1 contains the names of restaurants you have ordered from on Zomato, and set2 contains the names of restaurants you 
     have ordered from on Swiggy, find and print the union and intersection of these sets.
    Hint: Use the union() and intersection() methods of Python sets."""

set1 = {"Dominos", "McDonalds", "Subway", "Burger King"}
set2 = {"Subway", "Burger King", "KFC", "Pizza Hut"}

union_result = set1.union(set2)
intersection_result = set1.intersection(set2)

print("Union:", union_result)
print("Intersection:", intersection_result)