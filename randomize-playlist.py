import settings
import os
import sys
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Find the directory where the executable is running
if getattr(sys, 'frozen', False):
    # Running in a bundle (PyInstaller executable)
    app_dir = os.path.dirname(sys.executable)
else:
    # Running in a normal Python environment
    app_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to config.py (external)
config_path = os.path.join(app_dir, "settings.py")

# Check if the external config file exists
if not os.path.exists(config_path):
    raise FileNotFoundError("settings.py not found. Please place it in the same directory as the executable.")

# Load the config file dynamically using exec()
with open(config_path) as f:
    code = f.read()
    exec(code)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET,
                                                           redirect_uri=REDIRECT_URI,
                                                           scope="playlist-modify-public playlist-modify-private",
                                                           cache_path="./tokens.txt"))


def randomizer(playlist_id):
    # Get the tracks from the playlist
    tracks = sp.playlist(playlist_id)
    print(f"Randomizing playlist: {tracks['name']}")
    tracks = tracks["tracks"]["items"]
    tracks_ids = []
    for i in range(len(tracks)):
        track_id = tracks[i]['track']['id']
        tracks_ids.append(track_id)

    sp.playlist_remove_all_occurrences_of_items(playlist_id, tracks_ids)

    
    random.shuffle(tracks_ids)
    # Re-adding songs:
    for i in range(len(tracks_ids)):
        sp.playlist_add_items(playlist_id, [f"spotify:track:{tracks_ids[i]}"], position=i)


playlists = PLAYLISTS_TO_RANDOMIZE

for i in playlists:
    playlist_id = f'spotify:playlist:{i}'
    randomizer(playlist_id)
    print("Done!")
    