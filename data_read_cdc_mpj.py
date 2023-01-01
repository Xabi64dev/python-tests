#!/usr/bin/env ptyhon3
# coding: utf-8

import csv

with open('data_cdc_mpj.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv,delimiter=',')

    for ligne in reader:
        print("Ref: " + ligne['ref'] + "\nCategory: " + ligne['cat'] + "\nMaterial: " + ligne['material'])