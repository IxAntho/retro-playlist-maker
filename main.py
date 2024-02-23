import datetime
from data_manager import DataManager
from spotify_manager import SpotifyManager


def create_new_playlist(year):
    data = DataManager(year)
    songs = data.top_songs
    user = SpotifyManager()
    playlist_id = user.create_new_playlist(year)
    user.fill_in_playlist(songs, year, playlist_id)


date = input("what year you would like to travel to? Type the year in YYYY format: ")
today = datetime.date.today()
month = today.month
day = today.day

date_str = f"{date}-{month:02d}-{day:02d}"
create_new_playlist(date_str)
