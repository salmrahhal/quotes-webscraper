import requests
from bs4 import BeautifulSoup
import csv

quotes_details = []
page_number = 1 

while True:
    page = requests.get(f"https://quotes.toscrape.com/page/{page_number}/")
    soup = BeautifulSoup(page.content, "lxml")

    allQuotes = soup.find_all("div", {'class': 'quote'})

    if not allQuotes:
        break

    for i in allQuotes:
        text = i.find("span", {'class':'text'}).get_text()
        author = i.find("small", {'class':'author'}).get_text()
        tags = [t.get_text() for t in i.find_all("a", {'class':'tag'})]
        tags = "  ".join(tags) 

        quotes_details.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    print(f"page {page_number}")
    page_number += 1 

keys = quotes_details[0].keys()
with open("C:/Users/newtun/Desktop/quotes.csv", "w", newline='',encoding="utf-8") as f:
    writer = csv.DictWriter(f, keys)
    writer.writeheader()
    writer.writerows(quotes_details)

print("Done")

