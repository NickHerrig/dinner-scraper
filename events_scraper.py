from pprint import pprint

from bs4 import BeautifulSoup
import requests

from pyalert import send_message


url = 'https://ohospitality.com/events/'
r = requests.get(url)

html = BeautifulSoup(r.content, 'html.parser')

events = html.find_all('h3')
page_links = html.find_all('a')
purchase_links = []

for link in page_links:
    if link.string == 'Tickets + Menu':
        purchase_links.append(link['href'])

for event, link in zip(events, purchase_links):
    alert_subject = 'New Event!'
    alert_body ='Event Name: {event} \n Purchase Tickets Here: {link}'.format(event=event.string, link=link) 
    reciever = #TODO Replace with os env variable
    send_message(reciever, alert_subject, alert_body)
