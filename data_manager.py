import requests
from bs4 import BeautifulSoup

class DataManager:

    def __init__(self, date):
        self.soup = BeautifulSoup(self.get_html(date), "html.parser")
        self.top_songs = self.get_songs()

    def get_html(self, date):
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
        return response.text

    def get_songs(self):
        song_names_spans = self.soup.select("li ul li h3") # Here, when looking for an element, allways try to do it like cascading
        song_names = [song.getText().strip() for song in song_names_spans]
        return song_names
