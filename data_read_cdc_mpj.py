#!/usr/bin/env ptyhon3
# coding: utf-8

import csv

with open('data_cdc_mpj.csv') as fichier_csv:
    # taille = len(fichier_csv.readlines())
    reader = csv.DictReader(fichier_csv,delimiter=',')
    motif = input("Motif recherché.... ref or category: ")
    
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