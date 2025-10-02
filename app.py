import config
import functions as f
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

def main():
    left, center, right = st.columns([1,7,1])
    with center:
        st.title("🎵 Music recommender 🎵")

    # Log in Spotify API
    sp = sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id,
                                                           client_secret= config.client_secret))

    # Session set up
    if "trendy" not in st.session_state:
        # Session variables/dictionaries
        st.session_state.mood = ""
        st.session_state.trendy = f.find_top100()
        st.session_state.clustered_df = pd.read_csv("data/labeled_audio_features_dataset_curated.csv", index_col=0)
        st.session_state.cluster_labels = {
            "Instrumental":0,
            "Electronic sounds":1,
            "Sing along":2,
            "Slow beats":3,
            "Road Trip Mix":4
        }
        # Navigation
        st.session_state.recommend_trendy = False
        st.session_state.recommend_mood = False

    # App
    left, center, right = st.columns(3)
    if left.button("Recommend trendy song!"):
        st.session_state.recommend_trendy = True
        st.session_state.recommend_mood = False
        st.rerun()
    if right.button("Choose a mood"):
        st.session_state.recommend_trendy = False
        st.session_state.recommend_mood = True
        st.rerun()

    left, center, right = st.columns([2,5,2])
    # Recommend trendy song
    if st.session_state.recommend_trendy == True:
        with center:
            f.play_song(f.choose_random_trendy(sp, st.session_state.trendy))

    # Recommend 3 songs from clusters
    if st.session_state.recommend_mood == True:
        with center:
            st.session_state.mood = st.selectbox("Moods", [i for i in st.session_state.cluster_labels])
            if center.button("Recommend 3 songs!"):
                track_ids = []
                for i in range(3):
                    track_ids.append(st.session_state.clustered_df
                                     [st.session_state.clustered_df
                                      ['cluster']==
                                      st.session_state.cluster_labels[st.session_state.mood]]
                                      .sample()['track_id'].item())
                for i in track_ids:
                    f.play_song(i)




if __name__ == '__main__':
    main()