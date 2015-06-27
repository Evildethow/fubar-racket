from bs4 import BeautifulSoup

import requests
import os

r  = requests.get("http://www.abc.net.au/triplej/racket/playlists/s4260756.htm")

data = r.text

soup = BeautifulSoup(data)

def text_with_newlines(elem):
    text = ''
    for e in elem.recursiveChildGenerator():
        if isinstance(e, basestring):
            text += e.strip()
        elif e.name == 'br':
            text += '\n'
    return text
data = soup.find_all('span', {'class' : 'text'})
data.pop(0) # hack
for link in data:
	print(os.linesep.join([s for s in text_with_newlines(link).splitlines() if s]))

