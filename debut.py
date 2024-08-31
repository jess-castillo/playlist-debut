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

def generate_mixed_list_with_sum_limit(sum_limit):
    while True:
        # Calculate how many 3's will be in the list
        num_threes = 11  # 50% of 19 rounded down (which is 9)
        
        # Create the list with the appropriate number of 3's
        result_list = [3] * num_threes
        
        # Fill the rest with random choices of 2, 4, or 5
        remaining_numbers = 19 - num_threes
        result_list.extend(random.choices([2, 4], k=remaining_numbers))
        
        # Shuffle the list to mix the numbers up
        random.shuffle(result_list)
        
        # Check if the sum of the elements meets the sum limit
        if sum(result_list) <= sum_limit:
            return result_list


def insert_focus_song(mixed_list, focus_song_id, playlist_len):
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

# https://open.spotify.com/playlist/1LaFd5xbkkbRXrm7inRTq4?si=4189df3ea13f4a6e&pt=deaaa9830404dde380e432b8d693479e
# playlists = ['5U934d48njPvMoejeF4Lm0', '1LaFd5xbkkbRXrm7inRTq4']
playlists = ['1LaFd5xbkkbRXrm7inRTq4']
# 6afspjTp6s1QucDHVKPDss
focus_song_id = "6afspjTp6s1QucDHVKPDss"

for i in playlists:
    playlist_id = f'spotify:playlist:{i}'
    tracks = sp.playlist(playlist_id)
    print(f"Adding focus song to playlist: {tracks['name']}")
    playlist_len = len(tracks["tracks"]["items"])
    print(f"The lenght of the playlist is: {playlist_len}")
    mixed_list = generate_mixed_list_with_sum_limit(playlist_len)
    #mixed_list = 18*[3]
    insert_focus_song(mixed_list, focus_song_id, playlist_len)
    print("Done!\n")

