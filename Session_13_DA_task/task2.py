# Create a recursive function sum_playlist_durations(durations) that calculates the total duration of songs.

def sum_playlist_durations(durations):
    if durations == []:
        return 0

    return durations[0] + sum_playlist_durations(durations[1:])

playlist = [180, 240, 200, 300]
result = sum_playlist_durations(playlist)
print("Total Playlist Duration:", result, "seconds")