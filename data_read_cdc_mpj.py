#!/usr/bin/env ptyhon3
# coding: utf-8

import csv

with open('data_cdc_mpj.csv') as fichier_csv:
    # taille = len(fichier_csv.readlines())
    reader = csv.DictReader(fichier_csv,delimiter=',')
    motif = input("Search motif, ... ref or category : ")
    
    # taille = len(fichier_csv.readlines())
    # print(taille)
    for ligne in reader:
        # print(len(ligne))
        # print(ligne)
        valeurs = ligne.values()
        art = ligne.items()
        liste_valeurs = list(valeurs)
        """ print(valeurs)
        print(art)
        print(liste_valeurs) """
        # print("-" * 31 + liste_valeurs[2])
        for val in liste_valeurs:
            if motif in val:
                print("--> " + "Ref: " + ligne['ref'] + "\nCategory: " + ligne['cat'] + "\nMaterial:\n" + ligne['material'] + "\n" + "*" * 31)
            # print(ligne["ref"] + ligne['cat'] + ligne['material'] )
            else:
                continue