import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
from urllib.parse import urljoin

header={
   "User-Agent": UserAgent().random
}
url = "https://www.psypost.org/"
response = requests.get(url,headers=header)
soup = BeautifulSoup(response.text,"html.parser")

os.makedirs("Psychology",exist_ok=True)
anchor_tags = soup.find_all("a")
for i,anchor_tag in enumerate(anchor_tags):
    title = anchor_tag.text.strip()
    link = anchor_tag.get("href")
    
    if not link or link.startswith("#"):
         continue
    full_link = urljoin(url, link)

    if title and link:
        file_name = os.path.join("Psychology",f"title_{i}.txt")

        try:
            link_page_response = requests.get(full_link,headers=header)
            link_page_soup = BeautifulSoup(link_page_response.text,"html.parser")
            paragraphs = link_page_soup.find_all("p")
            with open(file_name, "w", encoding="utf-8") as file:
                    file.write(title + "\n")
                    for paragraph in paragraphs:
                         file.write(paragraph.text.strip() + "\n")
        except Exception as e:
             print(f"Error occured: {e}")