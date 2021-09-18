import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd


details ={"links":[]}


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)


driver.get("https://tech-labs.com/manufacturers/simspray")


soup = BeautifulSoup(driver.page_source, 'html.parser')
urls = [item.get("href") for item in soup.find_all("a")]
for url in urls:
    details["links"].append(url)



df = pd.DataFrame.from_dict(details,orient='index')
well = df.transpose()
well.to_csv('simspray.csv')
driver.close()
