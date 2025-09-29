import functions as f
import pandas as pd
import streamlit as st

def main():
    st.title("🎵 Music recommender 🎵")

    # Session set up
    if "genre" not in st.session_state:
        # Session variables
        st.session_state.genre = ""
        st.session_state.trendy = f.find_top100()

    st.session_state.genre = st.selectbox("Choose a genre", ["Trendy", "Other"])

    if st.session_state.genre == "Trendy":
        f.play_song()#song_id


if __name__ == '__main__':
    main()