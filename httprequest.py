import requests

def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text