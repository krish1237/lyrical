from settings import GENIUS_BASE_URL, LYRICAL_KEY
import requests
from bs4 import BeautifulSoup

def search_genius(name):
    search_url = GENIUS_BASE_URL + "/search"
    querystring = {"q":name}

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': LYRICAL_KEY
        }

    response = requests.request("GET", search_url, headers=headers, params=querystring)
    return response

def get_lyrics_url(name):
    response = search_genius(name)
    response = response.json()
    song_data_list = response["response"]["hits"]
    song_data = song_data_list[0]["result"]
    song_lyrics_url = song_data["url"]
    return song_lyrics_url    
   
def get_lyrics(name):
    url = get_lyrics_url(name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    lyrics = soup.find("div", class_="lyrics").get_text()
    return lyrics

# lyrics = get_lyrics("Everything at once")
# print(lyrics)