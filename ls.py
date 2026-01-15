def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"{target} found at position {i}"
    return f"{target} not found"

songs = ["Believer", "Closer", "Faded", "Perfect", "Shape of You"]
song_name = "Faded"

print(linear_search(songs, song_name))
