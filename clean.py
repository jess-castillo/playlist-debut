import pprint
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = 'playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="de31f3d0bec44126ab8346000d130097",
                                                           client_secret="af22e7ee7a6f400e845506fd033cee0f",
                                                           redirect_uri="http://localhost:3000",
                                                           scope="playlist-modify-public playlist-modify-private"))
playlists = ['1LaFd5xbkkbRXrm7inRTq4', '5kJGvbJ2ZmlHOVyBmyBl7f', '0tVwAPDbh9VVOh2VN3VSob', '0LgoFGaJAfVDjEaTcGFm0e']
track_id = ["6afspjTp6s1QucDHVKPDss", "6J2LdBN97cDWn0MLxYh9HB"]
# tracks = sp.playlist(playlist_id)
for i in playlists:
    playlist_id = f'spotify:playlist:{i}'
    results = sp.playlist_remove_all_occurrences_of_items(playlist_id, track_id)
    pprint.pprint(results)