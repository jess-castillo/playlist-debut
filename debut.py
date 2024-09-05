import json
import pdb
import random
import time
import spotipy
import settings
from spotipy.oauth2 import SpotifyOAuth

# Fuente: https://github.com/spotipy-dev/spotipy/tree/master

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings.CLIENT_ID,
                                                           client_secret=settings.CLIENT_SECRET,
                                                           redirect_uri=settings.REDIRECT_URI,
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
        if sum_limit < 50:
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


playlists = settings.PLAYLISTS_DEBUT
focus_song_id = settings.FOCUS_SONG_ID

for i in playlists:
    start = time.time()
    playlist_id = f'spotify:playlist:{i}'
    tracks = sp.playlist(playlist_id)
    print(f"Adding focus song to playlist: {tracks['name']}")
    playlist_len = len(tracks["tracks"]["items"])
    print(f"The lenght of the playlist is: {playlist_len}")
    mixed_list = generate_mixed_list_with_sum_limit(playlist_len)
    insert_focus_song(mixed_list, focus_song_id, playlist_len)
    delta = time.time() - start
    print(f"Done in {delta:.2f} seconds!\n")

