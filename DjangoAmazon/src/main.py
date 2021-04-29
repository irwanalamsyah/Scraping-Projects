import requests
from bs4 import BeautifulSoup
import lxml


url = 'https://www.amazon.com/Kindle-Paperwhite-Waterproof-Storage-International/dp/B07741S7Y8/ref=lp_6436113051_1_1'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
#     'Accept-Languange': 'en',
# }
#
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, 'lxml')
# # print(soup.prettify())
#
# # name = soup.select_one(selector="#title")
# name = soup.select_one(selector="#productTitle").getText()
# # menghilangkan white space
# name = name.strip()
# # print(name)
#
# price = soup.select_one(selector="#priceblock_ourprice").getText()
# # menghilangkan mata uang dollar, menjadikan float format
# price = float(price[1:])
# # print(price)

def get_link_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept-Languange': 'en',
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price

print(get_link_data(url))