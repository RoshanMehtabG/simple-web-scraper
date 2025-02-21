import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from fake_useragent import UserAgent
import time

time.sleep(5)
headers = {
    "User-Agent": UserAgent().random
}
url = "https://books.toscrape.com/"
response = requests.get(url,headers=headers)
try:
    soup = BeautifulSoup(response.text,"html.parser")
    headings = soup.find_all("h3")
    all_data = []
    for heading in headings:
        anchor_tags = heading.find_all("a")
        for anchor_tag in anchor_tags:
            title = anchor_tag.text.strip()
            link = anchor_tag["href"]
            if link:
                Book_detail_url = urljoin(url,link)
                response_detail_url = requests.get(Book_detail_url,headers=headers)
                Book_detail_soup = BeautifulSoup(response_detail_url.text,"html.parser")
                table = Book_detail_soup.find_all("tr")
                for data in table:
                    key = data.find("th").text.strip()
                    value = data.find("td").text.strip()
                    all_data.append([title,key,value])
    df = pd.DataFrame(all_data,columns=["Title","Atrribute","Information"])
    df.to_csv("Books.csv",mode="a",header=True,index=False, encoding="utf-8-sig")
except Exception as e:
    print(f"Couldn't fetch website: {e}")