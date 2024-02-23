# Retro Playlist Generator

## Overview

This application allows users to create playlists with popular songs from specific years. The user inputs the desired
year, and the app generates a Spotify playlist filled with the top songs from that year according to Billboard's Hot 100
list. If the playlist already exists, the program returns a message indicating that. The playlists are created under the
user's Spotify account and are publicly accessible. If a song cannot be found on Spotify, the application will inform
the user that the song was skipped.

## features

- Users can create a playlist of top songs from any year according to Billboard's Hot 100 list.
- The application checks if a playlist with the desired year's top songs already exists and will not create a duplicate
  playlist.
- Publicly accessible Spotify playlists are created under the user's account.
- Skips songs that are not found on Spotify.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have the necessary libraries installed by running pip install -r requirements.txt.
3. Create a .env file in the project's root directory with your Spotify credentials in the following format:

```env
SPOTIFY_CLIENT_ID=<Your Spotify Client ID>
SPOTIFY_CLIENT_SECRET=<Your Spotify Client Secret>
SPOTIFY_USERNAME=<Your Spotify Username>
```

4. Run main.py.
5. When prompted, input the desired year in YYYY format.
6. Check your Spotify account for the newly created playlist.

## File Structure

**main.py:** The main script that initiates the process by asking the user for input and then invoking the relevant
functions from data_manager.py and spotify_manager.py.<br>
**data_manager.py:** A data manager class that fetches the Billboard Hot 100 list for a specified date and extracts the
top songs.<br>
**spotify_manager.py:** A Spotify manager class that interacts with the Spotify API to create and populate playlists.

## APIs and Libraries

**spotipy:** A Python library for the Spotify Web API. <br>
**requests:** A Python library for making HTTP requests. <br>
**beautifulsoup4:** A Python library for parsing HTML.<br>
**python-dotenv:** A Python library for managing environment variables.
