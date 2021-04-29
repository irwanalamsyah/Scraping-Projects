from bs4 import BeautifulSoup
import lxml


with open('index.html', 'r') as file:
    body = file.read()

# import os
# path = os.getcwd()
# # getcwd() -> Return a unicode string representing the current working directory.
# print(path)
# html = os.path.join(path, 'index.html')
# print(html)
#
# with open(html, 'r') as file:
#     body = file.read()

soup = BeautifulSoup(body, 'lxml')
# print(soup)
print(soup.prettify())

# get the title
title = soup.title
print(title)
print(title.name)
print(title.getText())

# get paragraph
paragraph = soup.p
print(paragraph)
print(paragraph.name)
print(paragraph.getText())
print('----------------------')

# get the first div
firs_div = soup.find('div')
print(firs_div)
print(firs_div.getText())
print('----------------------')

# get all the divs
# all_divs = soup.find_all('div')
# print(all_divs)
# for div in all_divs:
#     print(div)
#     print('----------------------')

# get the first movie
# first_movie = soup.find('div', class_='movie')
first_movie = soup.select('.movie')[0]
print(first_movie)
print(first_movie.getText())

# get all movie
# all_movies = soup.find_all('div', class_='movie')
all_movies = soup.select(selector='.movie')
# print(all_movies)
for movie in all_movies:
    print('----------------- ')
    print(movie.getText())


# get all the links
links = soup.find_all('a')
for link in links:
    # print(link)
    # print(link.getText())
    print(link.get('href'))

# get element by id
movie_box = soup.select_one('#movie-box')
print(movie_box)
print(movie_box.getText())

# parent / children
parent = movie_box.parent
print(parent)
children = movie_box.children
for child in children:
    print(child)
    print('--')

