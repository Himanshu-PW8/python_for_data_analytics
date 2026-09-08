"""2.Create a Python program that takes the number of followers as input and uses if, elif, and else 
     to print 'Micro Influencer' if followers < 10,000, 'Rising Star' if between 10,000 and 100,000, 
     and 'Celebrity' if above 100,000."""

no_of_followers = int(input("Enter your no. of followers: "))

if no_of_followers < 10000:
    print("You are a microinfluencer")
elif no_of_followers > 1000 and no_of_followers < 100000:
    print("You are a Rising Star")
else:
    print("You are a celebrity")
    