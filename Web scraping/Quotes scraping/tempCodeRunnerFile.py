import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://quotes.toscrape.com/"
page = '/page/1/'
all_quotes = []
while page:
    response = requests.get(url+page)
    soup = BeautifulSoup(response.text,"html.parser")

    quotes = soup.find_all("div",class_="quotes")
    for quote in quotes:
        text = quote.find("span",class_="text").text
        author = quote.find("small",class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        all_quotes.append({"quote": text, "author": author, "tags": ",".join(tags)})
    next_button = quotes.find("li",class_="next")
    if next_button:
        page = quotes.find("a")["href"]
    else:
        break

df = pd.DataFrame(all_quotes)
df.to_csv("Quotes.csv")
print("Scraping completed!")