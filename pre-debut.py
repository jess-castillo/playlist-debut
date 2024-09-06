import sys
import os
import time
import settings
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Fuente: https://github.com/spotipy-dev/spotipy/tree/master
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
start = time.time()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET,
                                                           redirect_uri=REDIRECT_URI,
                                                           scope="playlist-modify-public playlist-modify-private"))



def insert_focus_song(mixed_list, focus_song_id, playlist_len):
    # pdb.set_trace()
    # Start by inserting the item at the first position
    sp.playlist_add_items(playlist_id, [f"spotify:track:{focus_song_id}"], position=0)
    playlist_len += 1
    current_position = 1  # We start with an offset of 1 because we added an item at the start

    # Insert items based on the mixed_list
    for value in mixed_list:
        current_position += value  # Move forward by the value in the mixed_list
        if current_position <= playlist_len:
            sp.playlist_add_items(playlist_id, [f"spotify:track:{focus_song_id}"], position=current_position)
            current_position += 1  # Move past the newly inserted item
            playlist_len += 1
        else:
            sp.playlist_add_items(playlist_id, [f"spotify:track:{focus_song_id}"])
            playlist_len += 1
            break


playlists = PLAYLISTS_PREDEBUT
focus_song_id = FOCUS_SONG_ID

for i in playlists:
    playlist_id = f'spotify:playlist:{i}'
    tracks = sp.playlist(playlist_id)
    print(f"Adding focus song to playlist: {tracks['name']}")
    playlist_len = len(tracks["tracks"]["items"])
    print(f"The lenght of the playlist is: {playlist_len}")
    mixed_list = 19*[2]
    insert_focus_song(mixed_list, focus_song_id, playlist_len)
    delta = time.time() - start
    print(f"Done in {delta:.2f} seconds!\n")