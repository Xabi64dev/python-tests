#!/usr/bin/env ptyhon3
# coding: utf-8

import csv
import re

with open('data_cdc_mpj.csv') as fichier_csv:
    # taille = len(fichier_csv.readlines())
    reader = csv.DictReader(fichier_csv,delimiter=',')
    motif = input("Motif recherché.... : ")
    
    # taille = len(fichier_csv.readlines())
    # print(taille)
    for ligne in reader:
        # print(len(ligne))
        # print(ligne)
        valeurs = ligne.values()
        if motif in valeurs:
            print("Ref: " + ligne['ref'] + "\nCategory: " + ligne['cat'] + "\nMaterial:\n" + ligne['material'] + "\n" + "*" * 31)
        else:
            continue
       #print(ligne.count(motif))
       #print(len(ligne.get("material").split("\n")))
    #print(ligne.get("material").split("\n")[0:])
       
""" if motif in ligne.values():
            print(ligne.values())
            print(ligne.items())
            print("\n"+"*" * 31)
            print("Ref: " + ligne['ref'] + "\nCategory: " + ligne['cat'] + "\nMaterial: " + "\n" + ligne['material'])
            print(ligne.get("material").split("\n"))
        if motif in ligne.get("material").split("\n"):
            print("False") """