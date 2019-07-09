import requests
from bs4 import BeautifulSoup # beautifulsoup4

def returnsoup(url):

    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    return soup

def returnhtml(url):

    soup = returnsoup(url)
    html = soup.text
    return html

def gethtmltag(url, copyselector):

    soup = returnsoup(url)
    tag = soup.select(copyselector)
    taglen = str(len(tag))
    return tag, taglen

def gethtmltagAttributes(url, copyselector, attribute):

    soup = returnsoup(url)
    tag = soup.select(copyselector)[0][attribute]
    return tag
