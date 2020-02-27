from pprint import pprint
import sys

from bs4 import BeautifulSoup
import requests

from pyalert import send_message


url = 'https://ohospitality.com/events/'

def fetch_html(url):
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError as error:
        print("Usually related to a network problem, (DNS failure, refused connection, etc)")
        raise SystemExit(error)

    if response.status_code != 200:
        raise SystemExit('Non 200 recieved from url endpoint. Status code: ', response.status_code)
    elif response.status_code == 200:
        return response.content

page_content = fetch_html(url)
html = BeautifulSoup(page_content, 'html.parser')

events = html.find_all('h3')
page_links = html.find_all('a')
purchase_links = []

for link in page_links:
    if link.string == 'Tickets + Menu':
        purchase_links.append(link['href'])

for event, link in zip(events, purchase_links):
    alert_subject = 'New Event!'
    alert_body ='Event Name: {event} \n Purchase Tickets Here: {link}'.format(event=event.string, link=link) 
#TODO    reciever = Replace with os env variable
    send_message(reciever, alert_subject, alert_body)
