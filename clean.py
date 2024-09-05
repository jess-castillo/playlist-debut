import settings

import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings.CLIENT_ID,
                                                           client_secret=settings.CLIENT_SECRET,
                                                           redirect_uri=settings.REDIRECT_URI,
                                                           scope="playlist-modify-public playlist-modify-private"))
playlists = settings.PLAYLISTS_TO_CLEAN
track_id = [settings.FOCUS_SONG_ID]


for i in playlists:
    playlist_id = f'spotify:playlist:{i}'
    tracks = sp.playlist(playlist_id)
    print(f"Deleting focus song to playlist: {tracks['name']}")
    sp.playlist_remove_all_occurrences_of_items(playlist_id, track_id)
