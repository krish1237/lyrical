from settings import AZLYRICS_URL

# TODO : query constructors
# def query_constructor_azlyrics(name, artist= None):
    
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.azlyrics.com/lyrics/alanwalker/lily.html")

soup = BeautifulSoup(response.content, 'html.parser')

#APPARENTLY FUCKIN ILLEGAL AND CROSS DOMAIN ISSUES
print(soup)