import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies = [movie.getText() for movie in soup.find_all(name='h3', class_='title')]
movies.reverse()
with open('movies.txt', 'w', encoding="utf-8") as file:
    for movie in movies:
        file.write(movie+'\n')
