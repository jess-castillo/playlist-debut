from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy
import time
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="de31f3d0bec44126ab8346000d130097",
                                                           client_secret="af22e7ee7a6f400e845506fd033cee0f",
                                                           redirect_uri="http://localhost:3000",
                                                           scope="playlist-modify-public playlist-modify-private"))
# https://open.spotify.com/playlist/7yKyeLJrUurzgpDI9rt4mF?si=6ba59d38355d4886
playlist_id = '7yKyeLJrUurzgpDI9rt4mF'
"""
results = sp.playlist_tracks(playlist_id)
tracks = results['items']
track_ids = [track['track']['id'] for track in tracks]
audio_features = sp.audio_features(track_ids)

# Create a DataFrame of audio features
df = pd.DataFrame(audio_features)
df = df[['danceability', 'energy', 'speechiness', 'acousticness',
         'instrumentalness', 'liveness', 'valence', 'tempo']]

# Generate a correlation matrix
correlation_matrix = df.corr()

# Plot the correlation matrix using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Show the plot
plt.show()
"""
tid = '6afspjTp6s1QucDHVKPDss'
start = time.time()
features = sp.audio_features(tid)
delta = time.time() - start
print(json.dumps(features, indent=4))
print(f"features retrieved in {delta:.2f} seconds")


start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(json.dumps(analysis, indent=4))
print(f"analysis retrieved in {delta:.2f} seconds")