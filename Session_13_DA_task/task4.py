# Create a recursive function count_likes(posts) that calculates likes across Instagram posts and all their nested replies.

def count_likes(posts):
    total = posts["likes"]

    for reply in posts["replies"]:
        total = total + count_likes(reply)

    return total


instagram_posts = {
    "likes": 100,
    "replies": [
        {
            "likes": 50,
            "replies": [
                {
                    "likes": 20,
                    "replies": []
                },
                {
                    "likes": 10,
                    "replies": []
                }
            ]
        },
        {
            "likes": 30,
            "replies": []
        }
    ]
}

result = count_likes(instagram_posts)
print("Total Likes:", result)