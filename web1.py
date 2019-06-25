import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', class_='wikitable')

for link in tb.find_all('b'):
    name = link.find('a')
    print(name.get_text('title'))

input("enter to exit")
