
import requests
from bs4 import BeautifulSoup
import pandas as pd
def fetch_weather():
    url = "https://www.timeanddate.com/weather/@11459741"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        Location = soup.find("h1",class_="headline-banner__title").text
        weather = soup.find("div",class_="bk-focus__qlook").text
        if Location and weather:
            Weather_info = Location + "-" + weather
            #pandas
            df = pd.DataFrame({"Weather info": [Weather_info]})
            df.to_csv("Weather.csv",index=False,encoding="utf-8")
            # To save information inside txt file enable this and disable pandas:
            # with open("file.txt","w",encoding="utf-8") as file:
            #     file.write(Weather_info)

            print("Weather data saved!")
        else:
            print("Could not find location or weather information on the page")
    except requests.exceptions.RequestException as e:
        print(f"request failed:{e}")
fetch_weather()