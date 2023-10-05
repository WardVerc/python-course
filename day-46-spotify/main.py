from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# ATTENTION!: Go to Spotify Developers, create a new app and copy Client ID + Client Secret to here:


SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIFY_REDIRECT_URI = "http://localhost/"

USER_ID = "31iozhjbaltxisdhzu5zlua6otye"
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"

# Authorize
scope = "user-library-read playlist-modify-private playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI))
# print(sp.current_user())

def get_liked_songs():
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

# Find track
def find_track(search: str):
    search_results = sp.search(q=search, type="track", limit=1)
    track_uri = search_results['tracks']['items'][0]['uri']
    print("Track URI: ", track_uri)
    return track_uri

# Create Playlist
def create_playlist(name: str, description: str, public=False):
    response = sp.user_playlist_create(user=USER_ID, name=name, public=public, description=description)
    print("Playlist id: ", response['id'])
    return response['id']

# Add tracks to playlist
def add_tracks_to_playlist(track_uris: list[str], playlist_id: str):
    response = sp.user_playlist_add_tracks(user=USER_ID, playlist_id=playlist_id, tracks=track_uris)
    print("Added tracks to playlist, ", response)

# Scrape top 100 songs from date
def scrape_100_songs_from_date(date: str):
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
    billboard = response.text
    soup = BeautifulSoup(billboard, "html.parser")
    list_items = soup.find_all(name="h3", id="title-of-a-story", class_="a-font-primary-bold-s")

    track_uris = []

    # first 2 title are "Gains in weekly.." and "Additional awards"
    for index, item in enumerate(list_items[2:]):
        # Remove some new line characters etc
        title = item.getText()[14:-4]
        artist = item.find_next_siblings("span")[0].getText()[4:-1]
        print(f"{index + 1}#")
        print(f"{artist} - {title}\n")
        uri = find_track(f"{artist} - {title}")
        track_uris.append(uri)

    return track_uris


date = input("Enter a date to get the top songs from that period, in the format yyyy-mm-dd: \n")
uris = scrape_100_songs_from_date(date)
id = create_playlist(name=f"Top 100 Billboard from {date}", description=f"Top 100 songs of {date}. Created with Python code.")
add_tracks_to_playlist(track_uris=uris, playlist_id=id)
