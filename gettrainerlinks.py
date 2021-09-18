#start here to get trainer files from each manufacterer url
import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd


details ={"links":[]}


driver = webdriver.Chrome()

pages = ["https://tech-labs.com/manufacturers/bayport-technical"]

# use this snippet for manufacterers with pagination
# ukurasa = ["https://tech-labs.com/manufacturers/amatrol?page=0%2C"]

# tejas = ["0","1","2","3","4","5","6","7","8"]

# for teja in tejas:
#     ukurasa.append(ukurasa[0]+teja)






for page in pages:   #replace with variable ukurasa in paginated pages

    driver.get(page)
   
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    urls = [item.get("href") for item in soup.find_all("a")]
    for url in urls:
        if "/products" in url:
            details["links"].append(url)
            print(url)



df = pd.DataFrame.from_dict(details,orient='index')
well = df.transpose()
well.to_csv('BAYPORT-AGAIN.csv')
driver.close()
