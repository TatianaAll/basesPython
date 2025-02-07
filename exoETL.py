import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
#print(page.content)

with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")
#print(soup)

#Récupérer le titre de la page
title = soup.title.string
#Les h1 avec la fonction find
h1 = soup.find("h1").string
#print(h1)

products = {}
description_list = []
temp_products = soup.find_all("li")
for product in temp_products:
    #nom du produit
    nameProduct = product.find("h2").string
    #prix
    priceProduct = product.find("p", class_="price").string
    priceList = priceProduct.split(" ")
    price = float(priceList[1])
    priceDollar = price * 1.2
    products[nameProduct + " price dollar"] = str(priceDollar) + "$"
    products[nameProduct + " price euro"] = str(price) + "€"

    #choper le dernier élément des p, c'est celui qui contient la description
    #mais dépendant de la structure HTML, c'est pas hyper robuste
    description = product.find_all("p")[-1].string
    products[nameProduct + " description"] = description

print(products)


