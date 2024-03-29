import re
import sys
import htmlparser

# ex) http://demo.testfire.net/login/login.jsp
def geturlinfo(url, str):
    domainp = '^(https?:\/\/)?([\da-z\.-]+)'
    domain = re.compile(domainp).match(url).group()
    middle = re.sub('^(https?:\/\/)', "", domain)
    current_pagep = '\/[a-zA-Z0-9]*\.[a-zA-Z0-9]*$'  # ex) /login.php

    if(str=="domain"):
        print("\nDomain = " + domain) # http://demo.testfire.net
        return domain

    elif(str=="middle"):
        print("Middle = " + middle)
        return middle # demo.testfire.net

    elif(str=="current_page"):
        try:
            current_page = re.compile(current_pagep).search(url).group()
            print("Current page = " + current_page)
            return current_page
        except AttributeError:
            print("The current page doesn't exist.")
            return 0

    elif(str=="path"):
        path = re.sub(current_pagep, "", url)  # ex) domain/login
        print("Path = " + path)
        return path

def getNextpage(url):

    soup = htmlparser.returnsoup(url)
    form_tag = soup.form
    action_page = form_tag.get('action')
    return action_page
