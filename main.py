import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
# print(movie_titles)     # prints movies ranked from 100 to 1
movies = movie_titles[::-1]   # slice operator reverses the order

# using for loop to reverse order
# for n in range(len(movie_titles) - 1, -1, -1):
#     print(movie_titles[n])

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

