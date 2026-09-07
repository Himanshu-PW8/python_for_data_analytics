"""Write a Python script that intentionally mixes tabs and spaces for indentation, 
   then fix the script so it runs without errors.Hint:Use only spaces for indentation, as per Python's
   best practices."""

# Incorrect Code
age = 20

if age >= 18:
	print("You are an adult")
    print("You can vote") # ye code galat hai kyunki pehle print ke aage TAB hai aur dusre print ke aage 4 spaces hain.

# Correct Code
age = 20

if age >= 18:
	print("You are an adult")
	print("You can vote") # This is Correct Code because only spaces are used.