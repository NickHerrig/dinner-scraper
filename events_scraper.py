from pprint import pprint

from bs4 import BeautifulSoup
import requests

url = 'https://ohospitality.com/events/'
r = requests.get(url)

html = BeautifulSoup(r.content, 'html.parser')

events = html.find_all('h3')
page_links = html.find_all('a')
purchase_links = []

for link in page_links:
    if link.string == 'Tickets + Menu':
        purchase_links.append(link['href'])
