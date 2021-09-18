import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

urls = ["https://tech-labs.com/products/denford-turn-370-pro-cnc-lathe"]

#If there is no such folder, the script will create one automatically
folder_location = r'F:\webscraperz'
if not os.path.exists(folder_location):os.mkdir(folder_location)

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")    
    for link in soup.select("a[href$='.pdf']"):
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
             f.write(requests.get(urljoin(url,link['href'])).content)