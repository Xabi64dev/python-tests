#!/usr/bin/env python3
# coding: utf-8

import csv

import requests
from bs4 import BeautifulSoup

# lien de la page à scrapper
url = "https://www.petitjean.com/online/fr/76-mouches-cdc-mp"
reponse = requests.get(url)
page = reponse.content

# affiche la page HTML
# print(page)

# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
# print(soup.find_all('a'))

# récupération de tous les titres
titres = soup.find_all("span",class_="editable")
titre_textes = []
for titre in titres:
	titre_textes.append(titre.string)


# récupération de toutes les descriptions et separation des catégories
descriptions = soup.find_all("p",class_="product-desc")
material_textes = []
catfly_textes = []
for description in descriptions:
	desc = description.string.strip()
	# print(description.string.strip())
	pos = desc.find("\n")
	catfly = desc[0:pos]
	material = desc.replace(catfly, '')
	catfly_textes.append(catfly.strip())
	material_textes.append(material.strip())
# print(description_textes)


 
# création du fichier data.csv
en_tete = ['ref', 'cat', 'description']
with open('data_cdc_desc.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow(en_tete)
	# zip permet d'itérer sur deux listes à la fois
	for ref,cat,description in zip(titre_textes,catfly_textes,material_textes):
		writer.writerow([ref,cat,description])
