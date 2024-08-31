import json
import pdb
import random

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Fuente: https://github.com/spotipy-dev/spotipy/tree/master

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="de31f3d0bec44126ab8346000d130097",
                                                           client_secret="af22e7ee7a6f400e845506fd033cee0f",
                                                           redirect_uri="http://localhost:3000",
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

# https://open.spotify.com/playlist/05qYM9xgYexlPa9y4o6mEk?si=1d65df5e828548e6
playlist_id = 'spotify:playlist:05qYM9xgYexlPa9y4o6mEk'
tracks = sp.playlist(playlist_id)
playlist_len = len(tracks["tracks"]["items"])
print(f"The lenght of the playlist is: {playlist_len}")

# https://open.spotify.com/track/6afspjTp6s1QucDHVKPDss?si=ef1466f1077e4171
focus_song_id = "6afspjTp6s1QucDHVKPDss"

mixed_list = 18*[3]

print("Adding focus song......")
insert_focus_song(mixed_list, focus_song_id, playlist_len)
print("Done!")

