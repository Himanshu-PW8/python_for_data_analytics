"""2.Create a Python program that takes the number of followers as input and uses if, elif, and 
else to print 'Micro Influencer' if followers < 10,000, 'Rising Star' if between 10,000 and 
100,000, and 'Celebrity' if above 100,000."""

followers = int(input("Enter the number of followers: "))
if followers < 10000:
    print("You are a Micro Influencer")
elif followers < 100000:
    print("You are a Rising Star")
else :
    print("You are a celebrity")