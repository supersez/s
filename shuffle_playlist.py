import json
import random
import os

def reverse_shuffle(playlist):
    return playlist[::-1]

def overhand_shuffle(playlist):
    shuffled = []
    while playlist:
        cut = random.randint(1, len(playlist))
        shuffled = playlist[:cut] + shuffled
        playlist = playlist[cut:]
    return shuffled

def riffle_shuffle(playlist):
    cut = len(playlist) // 2
    left, right = playlist[:cut], playlist[cut:]
    shuffled = []
    while left or right:
        if left:
            shuffled.append(left.pop(0))
        if right:
            shuffled.append(right.pop(0))
    return shuffled

def pile_shuffle(playlist):
    piles = [[] for _ in range(random.randint(2, 10))]
    while playlist:
        for pile in piles:
            if not playlist:
                break
            pile.append(playlist.pop(0))
    shuffled = [item for pile in piles for item in pile]
    return shuffled

def hindu_shuffle(playlist):
    return [playlist.pop(random.randint(0, len(playlist)-1)) for _ in range(len(playlist))]

def mongean_shuffle(playlist):
    return [playlist[i] for i in range(len(playlist)) if i % 2 == 1] + [playlist[i] for i in range(len(playlist)) if i % 2 == 0]

def faro_shuffle(playlist):
    half = len(playlist) // 2
    return [val for pair in zip(playlist[:half], playlist[half:]) for val in pair]

# Get the selected shuffle method from the environment variable
shuffle_method = os.getenv("shuffle_method")

with open("playlist.json", "r") as file:
    playlist = json.load(file)

# Call the selected shuffle method
shuffled_playlist = globals()[shuffle_method](playlist)

with open("playlist.json", "w") as file:
    json.dump(shuffled_playlist, file, indent=4)
