"""2.Write a function update_playlist_price(playlist, new_price) that updates the price of a given playlist in the playlist_prices 
     dictionary.Test it by updating the price of any one playlist and printing the updated dictionary."""

playlist_prices = {
    "Chill Hits": 99,
    "Top Hits": 129,
    "Workout Music": 149,
    "Love Songs": 79,
    "Party Hits": 119
}

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Chill Hits", 149)

print(playlist_prices)