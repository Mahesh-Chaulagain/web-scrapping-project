import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

print(soup.prettify())
# movies = soup.find_all(name="h3", class_="title")
# movie_list = []
# for movie in movies:
#     name = movie.getText()
#     movie_list.append(name)
#
# movie_rank = [int(rank.getText()[0] for rank in soup.find_all(name="h3", class_="title"))]
#
# highest = max(movie_rank)
# highest_rank = movie_rank.index(highest)
#
# print(movie_rank[highest_rank])
#
#
# print(movie)
