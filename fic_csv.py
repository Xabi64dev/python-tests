#!/usr/bin/env python3
# coding: utf-8

import csv

en_tete = ['canal','freq']
with open('freq.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    #reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
       #print ("Canal: " + ligne['Canal'] + " Fréquence CB: " + ligne['Normaux'] + " Fréquence 1x Sup: " + ligne['1x Supérieur'])
        print (ligne['Canal'])
        