from bs4 import BeautifulSoup
import pandas as pd
import requests

class get_songs():
    def __init__(self,country) -> None:
        self.country = country
        self.base_url = "https://spotifycharts.com/regional"
    
    def get_HTML(self):
        url = self.base_url + self.country + "/daily/latest"
        html = requests.get(url)
        return html
    
    def craw_page(self):
        html = self.get_HTML
        soup = BeautifulSoup(html.text, 'html.parser')


    def return_csv():
        location = "regional-global-daily-latest.csv"
        songs = pd.read_csv(location)
        songs = songs.iloc[1:]
        return songs

        