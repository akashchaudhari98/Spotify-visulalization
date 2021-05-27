import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint 


class spotify_api():
    def __init__(self) -> None:
        self.client_secret = "7d9ea87b31a34b5d986eae80e188a1e0"
        self.client_id = "e782933190054ce5a496138eaa535e11"
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
                             client_secret = self.client_secret, client_id = self.client_id))

    def get_audio_analysis(self,track_id):
        data = self.spotify.audio_analysis(track_id)
        return data
    
    def get_audio_features(self,track_id):
        data = self.spotify.audio_features(track_id)
        data = data[0]
        return data

if __name__== "__main__":
    spotifyAPI = spotify_api()
    track = ",https://open.spotify.com/track/4ZtFanR9U6ndgddUvNcjcG"
    features = spotifyAPI.get_audio_features(track)
    print(type(features))
    for key,val in features.items():
        print(key," : ",val)
    
    print(features)
