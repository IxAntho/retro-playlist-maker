import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv(".env")
client_id: str = os.getenv("SPOTIFY_CLIENT_ID")
client_secret: str = os.getenv("SPOTIFY_CLIENT_SECRET")
username: str = os.getenv("SPOTIFY_USERNAME")
redirect_uri = "http://example.com"

class SpotifyManager:

    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private playlist-modify-public",
                redirect_uri="http://example.com",
                client_id=client_id,
                client_secret=client_secret,
                show_dialog=True,
                cache_path="token.txt",
                username=username,
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def create_new_playlist(self, year):
        name = f"{year}'s retro playlist"
        playlists = self.sp.current_user_playlists()

        for playlist in playlists["items"]:
            if playlist["name"] == name:
                print("Playlist already exists")
                return

        playlist = self.sp.user_playlist_create(user=self.user_id, name=name, public=True,
                                                description=f"{year}'s top 100 songs")
        return playlist["id"]

    def fill_in_playlist(self, songs, date, playlist_id):
        year = date.split("-")[0]
        print(year)
        song_uris = []
        for song in songs:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        # Use the Spotipy client to add tracks
        self.sp.playlist_add_items(playlist_id, song_uris)
