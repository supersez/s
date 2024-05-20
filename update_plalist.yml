name: Update Playlist

on:
  schedule:
    - cron: '0 6 * * *'  # Runs at 6:00 AM UTC which is 12:00 PM India Standard Time

jobs:
  update-playlist:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Shuffle playlist
      run: |
        python3 -c "
import json
import random

with open('playlist.json', 'r') as file:
    playlist = json.load(file)

random.shuffle(playlist)

with open('playlist.json', 'w') as file:
    json.dump(playlist, file, indent=4)
        "

    - name: Commit and push changes
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'
        git add playlist.json
        git commit -m 'Shuffle playlist'
        git push
