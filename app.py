import config
import functions as f
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

def main():
    st.title("🎵 Music recommender 🎵")

    # Log in Spotify API
    sp = sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id,
                                                           client_secret= config.client_secret))

    # Session set up
    if "genre" not in st.session_state:
        # Session variables
        st.session_state.genre = ""
        st.session_state.trendy = f.find_top100()

    # App
    left, center, right = st.columns([1,3,1])
    with center:

        st.session_state.genre = st.selectbox("Choose a genre", ["Trendy", "Other"], placeholder="Choose a genre")

        if center.button("Recommend!"):
            if st.session_state.genre == "Trendy":
                f.play_song(f.choose_random_song(sp, st.session_state.trendy))
            else:
                st.text("Other genres will be added soon!")


if __name__ == '__main__':
    main()