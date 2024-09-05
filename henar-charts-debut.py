import  time
import settings
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Fuente: https://github.com/spotipy-dev/spotipy/tree/master

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings.CLIENT_ID,
                                                           client_secret=settings.CLIENT_SECRET,
                                                           redirect_uri=settings.REDIRECT_URI,
                                                           scope="playlist-modify-public playlist-modify-private"))

def insert_focus_song(mixed_list, focus_song_id, playlist_len):
    # Start by inserting the item at the first position
    sp.playlist_add_items(playlist_id, [f"spotify:track:{focus_song_id}"], position=1)
    playlist_len += 1
    current_position = 2  # We start with an offset of 1 because we added an item at the start

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


playlists = settings.HENAR_CHARTS_DEBUT

focus_song_id = settings.FOCUS_SONG_ID

for i in playlists:
    start = time.time()
    playlist_id = f'spotify:playlist:{i}'
    tracks = sp.playlist(playlist_id)
    print(f"Adding focus song to playlist: {tracks['name']}")
    playlist_len = len(tracks["tracks"]["items"])
    mixed_list = 19*[3]
    insert_focus_song(mixed_list, focus_song_id, playlist_len)
    delta = time.time() - start
    print(f"Done in {delta:.2f} seconds!\n")

