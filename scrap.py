from bs4 import BeautifulSoup
import requests
#import selenium
from bs4 import BeautifulSoup


url_base = "https://github.com/explore"

site = requests.get(url_base)
siteSoup = BeautifulSoup(site.text, 'html.parser')

print(siteSoup.prettify())