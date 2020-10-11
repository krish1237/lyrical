from settings import GENIUS_BASE_URL, LYRICAL_KEY
import requests
from bs4 import BeautifulSoup
import logging

def search_genius(name):
    search_url = GENIUS_BASE_URL + "/search"
    querystring = {"q":name}

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': LYRICAL_KEY
        }

    logging.info("Sending Genius API request")
    response = requests.request("GET", search_url, headers=headers, params=querystring)
    logging.info("Received Genius API response")

    return response

def get_lyrics_url(name):
    response = search_genius(name)
    response = response.json()
    logging.info("Extracting Song Lyrics URL")
    song_data_list = response["response"]["hits"]
    song_data = song_data_list[0]["result"]
    song_lyrics_url = song_data["url"]
    logging.info("Song lyric url found : "+song_lyrics_url)
    return song_lyrics_url    

def scrape_lyrics(url):
    response = requests.get(url)
    logging.info(response.status_code)
    soup = BeautifulSoup(response.text,"html.parser")
    lyrics = soup.find("div", class_="lyrics").get_text()
    return lyrics
   
def get_lyrics(name):
    try:
        url = get_lyrics_url(name)
    except IndexError:
        logging.error("Lyrics not found")
        return "Lyrics not found" 
    logging.info("Scraping URL for lyrics")
    count = 0
    lyrics = ""
    while(count != 5):
        try:
            logging.info("Scraping Lyrics attempt:"+str(count+1))
            lyrics = scrape_lyrics(url)
            count = 5
        except:
            count+=1
            logging.info("Lyrics Scraping Failed. Trying again...")
            if(count == 5):
                raise ValueError
            continue
        break
    logging.info("Lyrics found")
    return lyrics