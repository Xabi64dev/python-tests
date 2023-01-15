#!/usr/bin/env python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def calc_wl(in_freq):
    '''
    Quand le bouton est cliqué
    '''
    band = builder.get_object('label_calc_band')
    result = builder.get_object('label_calc_wl')
    band_lincoln = builder.get_object('label_band')
    info = builder.get_object('label_info')
    freq = in_freq.get_text()
    wl = str(round(300/float(freq)))
    result.set_text(wl)
    # La bande CB "Normal"
    if 26.965 <= float(freq) <= 27.405:
        band.set_text('CB')
        band_lincoln.set_text('BANDE : A')
        info.set_text('26.965 à 27.405 MHz\nBande CB')
    # Les Supérieurs
    elif 27.405 < float(freq) <= 27.855:
        band.set_text('1x Sup')
        band_lincoln.set_text('BANDE : B')
        info.set_text('27.415 à 27.855 MHz')
    elif 27.865 <= float(freq) <= 28.305:
        band.set_text('2x Sup')
        info.set_text('27.865 à 28.305 MHz\nR.A 28.005 à 28.305 MHz')
        band_lincoln.set_text('BANDE : D')
    elif 28.315 <= float(freq) <= 28.755:
        band.set_text('3x Sup')
        band_lincoln.set_text('BANDE : F')
        info.set_text('28.315 à 28.755 MHz\nR.A')
    elif 28.765 <= float(freq) <= 29.205:
        band.set_text('4x Sup')
        band_lincoln.set_text('BANDE : H')
        info.set_text('28.765 à 29.205 MHz\nR.A')
    elif 29.215 <= float(freq) <= 29.655:
        band.set_text('5x Sup')
        band_lincoln.set_text('BANDE : I')
        info.set_text('29.215 à 29.655 MHz\nR.A')
    elif 29.665 <= float(freq) <= 30.105:
        band.set_text('6x Sup')
        band_lincoln.set_text('BANDE : J')
        info.set_text('29.665 à 30.105 MHz\nR.A 29.665 à 29.695 MHz')
    # Les inférieurs
    elif 26.515 <= float(freq) <= 26.955:
        band.set_text('1x Inf')
        band_lincoln.set_text('BANDE : C')
    elif 26.065 <= float(freq) <= 26.505:
        band.set_text('2x Inf')
        band_lincoln.set_text('BANDE : E')
        info.set_text('26.065 à 26.905 MHz\nTel sans fil\n26.305 à 26.495 MHz')
    elif 25.615 <= float(freq) <= 26.055:
        band.set_text('3x Inf')
        band_lincoln.set_text('BANDE : G')
    elif 25.165 <= float(freq) <= 25.605:
        band.set_text('4x Inf')
        band_lincoln.set_text('BANDE : K')
    elif 24.715 <= float(freq) <= 25.155:
        band.set_text('5x Inf')
        band_lincoln.set_text('BANDE : L')
        info.set_text('24.715 à 25.155 MHz R.A 24.895 à 24.995 MHz')
    else:
        band.set_text('No Band !!!')

    print(wl)

# inspiré de https://zestedesavoir.com/tutoriels/870/des-interfaces-graphiques-en-python-et-gtk/1456_utilisation-avancee/5778_prise-en-main-de-glade/
builder = Gtk.Builder()
builder.add_from_file('glade/Freq_01.glade')  # Rentrez évidemment votre fichier, pas le miens!

window = builder.get_object('main_window')
# Peut se faire dans Glade mais je préfère le faire ici, à vous de voir
window.connect('delete-event', Gtk.main_quit)



# Le handler
handler_01 = {'on_button_calc_clicked': calc_wl}
builder.connect_signals(handler_01)

window.show_all()
Gtk.main()