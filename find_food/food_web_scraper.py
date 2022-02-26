from pip import main
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import json

def get_collection():
    CONNECTION_STRING = ''
    client = MongoClient(CONNECTION_STRING)
    return client['LikedFood']

def add_food(food):
    collection = get_collection()
    collection.members.createIndex({"name": food})

# TO DO: remove favorite food

# TO DO: return a list of todays list that only contains liked food

def get_site(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    return result


def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find("ul", {"class": "meal-list horizontal-list"})
    
    for li in ul.find_all("li"):
        if li['class'] != ['shortmenucats']: 
            print(li.text)
        

if __name__ == "__main__":
    html = get_site( "https://menu.mtholyoke.edu/shortmenu.aspx?sName=Mount+Holyoke+College+Dining+Services&locationNum=40&locationName=Classics&naFlag=1&dtdate=2%2f23%2f2022&mealName=Breakfast").text
    scrape(html)

