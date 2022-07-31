from os import path
from flask import Flask, render_template
from bs4 import BeautifulSoup
import shutil
import requests

# Urls
url_base = "https://apod.nasa.gov/apod/"
src = requests.get(url_base + "astropix.html").text

# Soup
soup = BeautifulSoup(src, 'lxml')
center = soup.select('body > center')[2]
yesterday = center.find('hr').findNext('a').attrs['href']
img = soup.select('body > center > p')[1].find('a')

url_ext = img.attrs['href']
full_url = url_base + url_ext

# Today's picture
r = requests.get(full_url, stream=True)
if r.status_code == 200:
    file = open("./static/downloads/potd_nasa.jpg", "wb")
    file.write(r.content)
    file.close()

# Last 5 days
for i in range(5):
    prev_page = url_base + yesterday
    src = requests.get(prev_page).text
    soup = BeautifulSoup(src, 'lxml')

    center = soup.select('body > center')[2]
    yesterday = center.find('hr').findNext('a').attrs['href']
    img = soup.select('body > center > p')[1].find('a')

    url_ext = img.attrs['href']
    full_url = url_base + url_ext

    img_path = "./static/downloads/yesterday_potd_" + str(i+1) + ".jpg"
    r = requests.get(full_url, stream=True)
    if r.status_code == 200:
        file = open(img_path, "wb")
        file.write(r.content)
        file.close()


# Flask 
app = Flask(__name__)

@app.route('/')
def index():
    head = soup.select('body > center')[0].find('h1').text
    return render_template('index.html', **locals())

app.run(debug=True)
