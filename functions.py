from bs4 import BeautifulSoup
from IPython.display import IFrame
import pandas as pd
import requests

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
    return IFrame(src="https://open.spotify.com/embed/track/"+track_id,
       width="320",
       height="80",
       frameborder="0",
       allowtransparency="true",
       allow="encrypted-media",
      )