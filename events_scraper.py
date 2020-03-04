from collections import namedtuple
import os
import sys

from bs4 import BeautifulSoup
import requests

from pyalert import send_message


url = 'https://ohospitality.com/events/'
alert_subject = 'New Event!'
reciever = password = os.environ['NICK_PERSONAL_PHONE']


def parse_events(page_content):
    html = BeautifulSoup(page_content, 'html.parser')    
    event_names = html.find_all('h3')
    page_links = html.find_all('a')
    event_links = []
    for link in page_links:
        if link.string == 'Tickets + Menu':
            event_links.append(link['href'])
    Event = namedtuple('Event', 'name link')
    for name, link in zip(event_names, event_links):
       yield Event(name.string, link) 

def craft_message(event):
    return 'Name: {event} \n link: {link}'.format(event=event.name, link=event.link) 

def main():
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError as error:
        print("Usually related to a network problem, (DNS failure, refused connection, etc)")
        raise SystemExit(error)
    
    if response.status_code != 200:
        raise SystemExit('Non 200 recieved from url endpoint. Status code: ', response.status_code)
    elif response.status_code == 200:
        for event in parse_events(response.content):
            send_message(reciever, alert_subject, craft_message(evnt)) 
            # TODO Check DB, if not present, send message, add to db

if __name__ == '__main__':
    main()
