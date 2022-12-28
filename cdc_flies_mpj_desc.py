#!/usr/bin/env python3
# coding: utf-8

import csv
import linecache

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
	# print(titre.string)
	titre_textes.append(titre.string)
# print(titre_textes)

# récupération de toutes les descriptions
descriptions = soup.find_all("p",class_="product-desc")
description_textes = []
for description in descriptions:
	# print(description.string.strip())
	description_textes.append(description.string.strip())
# print(description_textes)


 
# création du fichier data.csv
en_tete = ['ref', 'description']
with open('data_cdc_desc.csv', 'w') as fichier_csv:
	writer = csv.writer(fichier_csv, delimiter=',')
	writer.writerow(en_tete)
	# zip permet d'itérer sur deux listes à la fois
	for ref,description in zip(titre_textes,description_textes):
		writer.writerow([ref,description])


with open('data_cdc_desc.csv') as fichier:
	reader = csv.DictReader(fichier, delimiter=',')
	for ligne in reader:
		desc = ligne['description']
		print(desc)