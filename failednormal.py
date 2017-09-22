from bs4 import BeautifulSoup
import requests

def get_page(url):
    r = requests.get(url)
    data = r.content
    return data

def get_soup(data):
    soup = BeautifulSoup(data, "html.parser")
    return soup

def get_link(soup):
    return soup.find_all('a')[5]['href']

def make_article(soup):
    return soup.find('article').text.encode('utf-8')

page = get_page('https://www.failednormal.com/')
soup = get_soup(page)
link = get_link(soup)
page = get_page(link)
soup = get_soup(page)
article = make_article(soup)
