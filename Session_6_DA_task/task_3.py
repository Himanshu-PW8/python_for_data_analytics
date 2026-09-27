"""3.Remove a playlist from the playlist_prices dictionary using the del statement. Print the dictionary after deletion to confirm the 
     change."""

playlist_prices = {
    "Chill Hits": 99,
    "Top Hits": 129,
    "Workout Music": 149,
    "Love Songs": 79,
    "Party Hits": 119
}

del playlist_prices["Love Songs"]

print(playlist_prices)
