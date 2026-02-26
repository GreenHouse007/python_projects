from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

# I had to use selenium because the empireonline website is javascript rendered

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

driver = webdriver.Chrome()
driver.get(URL)

time.sleep(5)  # allow JS to load page

soup = BeautifulSoup(driver.page_source, "html.parser")


movies = soup.find_all("h2")

movie_titles = [movie.getText() for movie in movies if movie.getText().strip()]

movie_lines = []
for t in movie_titles:
    t = t.strip()
    # match lines like: 100) Avatar (2009)
    if re.match(r"^\d{1,3}\)\s.+\(\d{4}\)$", t):
        movie_lines.append(t)

movie_lines.sort(key=lambda s: int(s.split(")")[0]))

with open("movies.txt", "w", encoding="utf-8") as file:
    for line in movie_lines:
        file.write(line + "\n")

driver.quit()
