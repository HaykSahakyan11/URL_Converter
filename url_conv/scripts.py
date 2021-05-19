from bs4 import BeautifulSoup
import requests
import re


def find_name_from_url(url):
    try:
        url_modif = url.strip()
        source = requests.get(url_modif, verify=False).text
        soup = BeautifulSoup(source, 'lxml')
        head = soup.find('head')
        name = head.title.text
    except:
        name = "Not Found"
        raise Exception
    return name