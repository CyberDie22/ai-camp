import sys
import os
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"
}

# replace with url you want to scrape
#url = "https://garden.org/plants/view/181506/Roses-Rosa/"
#url = "https://garden.org/plants/view/530825/Peonies-Paeonia/"

url = sys.argv[1]

html = requests.get(url, headers=headers).content

soup = BeautifulSoup(html, 'html.parser')

header = soup.find("h1", "page-header")
name = header.text.split("(")[1].replace(")", "")
#name = "Sempervivum"
imgs = soup.find_all("img", "card-img-top")

imgurls = []
for img in imgs:
    imgurls.append("https://garden.org" + img.get("src"))
print(len(imgurls))
imgurls = imgurls[0:250]

if not os.path.exists(f"./imgs/{name}/"):
    os.makedirs(f"./imgs/{name}/")
for index, imgurl in enumerate(imgurls):
    print(f"Getting image {index} for species {name}")
    content = requests.get(imgurl, headers=headers).content
    with open(f"./imgs/{name}/{index}.jpg", "wb") as f:
        f.write(content)
