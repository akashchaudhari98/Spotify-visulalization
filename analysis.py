from numpy.lib.function_base import median
from spotify_APIcall import spotify_api
from get_songs import get_songs
import pandas as pd

class analysis_:
    def __init__(self):
        self.get_songs = get_songs("india")
        self.spotify = spotify_api()

    def get_song_id(self):
        songs_df = get_songs.return_csv()
        
        return songs_df

    def get_songs_audio_features(self,track_id):
        features_dict = self.spotify.get_audio_features(track_id)
        return features_dict

    def create_df(self):
        songs_df = self.get_song_id()
        danceability_,energy_,loudness_,speechiness_,acousticness_,instrumentalness_,liveness_,valence_,tempo_,duration_ = [],[],[],[],[],[],[],[],[],[]
        for idx,music in songs_df.iterrows():
            url = music['Unnamed: 4']
            features = self.get_songs_audio_features(url)
            danceability = features['danceability']
            energy = features['energy']
            loudness = features['loudness']
            speechiness = features['speechiness']
            acousticness = features['acousticness']
            instrumentalness = features['instrumentalness']
            liveness = features['liveness']
            valence = features['valence']
            tempo = features['tempo']
            #duration = features['duration']

            danceability_.append(danceability)
            energy_.append(energy)
            loudness_.append(loudness)
            acousticness_.append(acousticness)
            instrumentalness_.append(features)
            liveness_.append(liveness)
            valence_.append(valence)
            tempo_.append(tempo)
            #duration_.append(duration)
            speechiness_.append(speechiness)

        songs_df['danceability'] = danceability_
        songs_df['energy'] = energy_
        songs_df['loudness'] = loudness_
        songs_df['speechiness'] = speechiness_
        songs_df['acousticness'] = acousticness_
        songs_df['instrumentalness'] = instrumentalness_
        songs_df['liveness'] = liveness_
        songs_df['valence'] = valence_
        songs_df['tempo'] = tempo_
        #songs_df['duration'] = duration_

        return songs_df

    def mean(self):
        songs_df = self.create_df()
        list_tempo= []
        for idx,music in songs_df.iterrows():
            features = music['features']
            


if __name__ == "__main__":
    analysis = analysis()
    analysis.mean()
    