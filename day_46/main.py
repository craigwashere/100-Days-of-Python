import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:3000/'

date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
SONG_YEAR = date.split("-")[0]
print(f"song year: {SONG_YEAR}")

print("getting songs...")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, 'html.parser')

print("Parsing songs...")
titles = []
for song in soup.select("div ul li ul li"):
    try:
        title = song.h3.string.strip()
        artist = song.span.string.strip()
        titles.append({'title': title, 'artist': artist})
    except AttributeError:
        pass

def fetch_playlist_id(playlist_name):
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            return playlist['id']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
           client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, 
           scope='playlist-modify-public', cache_path="token.txt"))
    
user = sp.current_user()
user_id = sp.me()['id']

print("Checking for playlist")
playlist_id = fetch_playlist_id(f"jams from {SONG_YEAR}")
if playlist_id == None:
    playlist_id = sp.user_playlist_create(user_id, f"jams from {SONG_YEAR}")['id']

print("looking for songs")
song_uris = []    
skipped = 0
for title in titles:
    spotify_result = sp.search(q=f"artist:{title['artist']} track:{title['title']}", type="track")
    try:
        song_uri = spotify_result['tracks']['items'][0]['uri']
        #sp.user_playlist_add_tracks(user_id, playlist_id, [result['tracks']['items'][0]['uri']])
        song_uris.append(song_uri)
    except IndexError:
        print(f"{title['title']} doesn't exist in Spotify. Skipped.")
        skipped += 1

print("adding songs to playlist")
sp.user_playlist_add_tracks(user_id, playlist_id, song_uris)


