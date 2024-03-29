import requests

def send_post(data, next_url):

    # data example
    # data = {
    #           id_value: 'id',
    #           pw_value: 'donecare'
    # }

    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
    }

    resp = requests.post(next_url, data=data, headers=header)
    print("Send post packet")
    return resp
    # If you get response html code, use print(resp.text) code.
