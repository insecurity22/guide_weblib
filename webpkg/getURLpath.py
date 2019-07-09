import re
import sys
import htmlparser, helper

# ex) http://domain/login/login.php
def getDomainandMiddle(url):

    domainpattern = '^(https?:\/\/)?([\da-z\.-]+)' # Domain
    domain = re.compile(domainpattern).match(url).group()
    print("\nDomain = " + domain)

    middle = re.sub('^(https?:\/\/)', "", domain) # Except http://
    print("Middle = " + middle)

    return domain, middle


def getCurrentPage(url):

    current_page_p = '\/[a-zA-Z0-9]*\.[a-zA-Z0-9]*$' # ex) /login.php
    try:
        current_page = re.compile(current_page_p).search(url).group()
        print("Current page = " + str(current_page))
    except AttributeError:
        print("The current page doesn't exist.")

    path = re.sub(current_page_p, "", url) # ex) domain/login
    print("Path = " + path)

    return current_page, path


def getNextpage(url):

    soup = htmlparser.returnsoup(url)
    form_tag = soup.form
    action_page = form_tag.get('action')

    return action_page
