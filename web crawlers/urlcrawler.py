# retrieves all anchor tags in a website

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def urls():
    links=list()
    url = input('Enter-')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        href=tag.get('href', None)
        if href.startswith('https:') or href.startswith('http') or href.startswith('www'):
            links.append(href)
    
    return links


print(urls())