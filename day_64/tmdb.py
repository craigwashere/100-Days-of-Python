import requests

API_KEY = ''
API_URL = 'https://api.themoviedb.org/3/'

class TMDB:
    def search_movie(self, search_string):
        params = {'api_key': API_KEY, 'query': search_string}
        return  requests.get(f"{API_URL}/search/movie", params=params).json()['results']
        
    def find_movie(self, movie_id):
        params = {'api_key': API_KEY}
        return  requests.get(f"{API_URL}/movie/{movie_id}", params=params).json()