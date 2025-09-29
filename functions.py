from bs4 import BeautifulSoup
import pandas as pd
import random
import requests
import streamlit as st

def find_top100():
    url = "https://www.billboard.com/charts/hot-100/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    titles = []
    artists = []
    for song in soup.select("ul.o-chart-results-list-row li ul li h3"):
        titles.append(song.get_text().strip())
    for artist in soup.select("ul.o-chart-results-list-row li ul li span.a-no-trucate"):
        artists.append(artist.get_text().strip())
    
    top100 = pd.DataFrame({
        "title":titles,
        "artist":artists
    })

    return top100

def play_song(track_id):
    embed_url = f"https://open.spotify.com/embed/track/{track_id}"
    st.components.v1.iframe(embed_url, width="stretch", height="stretch")

def choose_random_song(sp, genre_df):
    song_title = random.choice(genre_df['title'])
    song_info = sp.search(q=song_title,limit=5,market="GB")
    track_id = song_info["tracks"]["items"][0]["id"]
    return track_id