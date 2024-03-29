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

    # F12 - copy selector
    # copyselector ex) form input[type=password]

    soup = returnsoup(url)
    tag = soup.select(copyselector)
    taglen = str(len(tag))
    return tag, taglen

def gethtmltagfirstAttributes(url, copyselector, attribute):

    soup = returnsoup(url)
    tag = soup.select(copyselector)[0][attribute]
    return tag

def gethtmltagAttributes(url, copyselector, attribute): # ex) form tag, action attribute

    soup = returnsoup(url)
    attribute_list = []
    for tag in soup.find_all(copyselector):
        attribute_list.append(tag.get(attribute))
    return attribute_list

