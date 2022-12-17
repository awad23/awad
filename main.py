from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/p/pl?N=100007709&SrchInDesc=3060&Order=1&PageSize=96"
result = requests.get(url)

doc = BeautifulSoup(result.content, "html.parser")

cards = doc.find_all(class_="item-cell")

for card in cards:
    print("-"*50)
    try:
        print(cards.index(card)+1)
        print("Name:", card.find(class_="item-info").find_all('a')[-2].text)
        print("price:", card.find(class_="price-current").strong.text)

    except:
        continue





