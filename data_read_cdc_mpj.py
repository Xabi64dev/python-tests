#!/usr/bin/env ptyhon3
# coding: utf-8

import csv
motif = input("Search motif, ... ref or category : ")
def cherche(motif):
    with open('data_cdc_mpj.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv,delimiter=',')
        for ligne in reader:
            valeurs = ligne.values()
            liste_valeurs = list(valeurs)
            for val in liste_valeurs:
                if motif in val:
                    print("\n--> " + "Ref: " + ligne['ref'] + "\nCategory: " + ligne['cat'] + "\nMaterial:\n" + ligne['material'] + "\n" + "*" * 31)
                else:
                    continue
cherche(motif)