#!/usr/bin/env python3
# coding: utf-8

import glob
import json
import os

path = input("Chemin absolue vers le dossier : ")
motif_cover = path + "/*.jpg"
motif_book = path + "/*.pdf"
print(motif_cover)
print(motif_book)
# list_fic_cover = glob.glob(path)
list_fic = sorted(os.listdir(path))
print(list_fic)
# print(list_fic_cover)
fic_cover = sorted(glob.glob(motif_cover))
fic_book = sorted(glob.glob(motif_book))
# book_items = [{'libraryName': 'My Library'}]
my_ebooks = {}
# my_ebooks["shelf"] = list()
my_ebooks_items = []

with open("list_fic.json", "w") as lf:
        
        for cover, ebook in zip(fic_cover, fic_book):
            fic_ebook_cover = os.path.basename(cover)
            fic_ebook = os.path.basename(ebook)
            fic_ebook_title = fic_ebook_cover.replace("_", " ")
            fic_ebook_title = fic_ebook_title.replace(".jpg", "")
            # my_ebooks.clear()
            # my_ebooks["couvFile"] = os.path.basename(cover)
            # my_ebooks["bookFile"] = os.path.basename(ebook)
            print(fic_ebook_title)
            print(fic_ebook_cover)
            print(fic_ebook)
            my_ebooks["ebookTitle"] = fic_ebook_title
            my_ebooks["couvFile"] = fic_ebook_cover
            my_ebooks["ebookFile"] = fic_ebook
            # book_items.append(my_ebooks)
            # print(type(my_ebooks))
            # print(book_items)
            # my_ebooks_items.append(my_ebooks)
            # obj = json.dumps(my_ebooks)
            # print(obj)
            json.dump(my_ebooks, lf)
                # print(my_books)

"""  my_books["ebookCover"] = fic_ebook_cover
    my_books["ebookFile"] = fic_ebook
    my_ebooks["shelf"].append(my_books) """
    

""" my_books = {}
for fic in list_fic_cover:
    my_books["book_cover"] = fic
    print(my_books) """

""" """
