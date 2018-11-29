#!/usr/bin/python
# Menulis data ke dalam berkas
berkas = open('L200180149', 'w')
berkas.write("L200180149\n")
berkas.write("10-25-1999\n")
berkas.write("Nur Fauzi Saputro\n")
berkas.write("Klaten\n")
berkas.close()

import shelve
b = open('L200180149', 'r')
NIM = b.readline()
TL = b.readline()
Nama = b.readline()
Kota = b.readline()
print Nama
print Kota, TL
print NIM
berkas.close()
