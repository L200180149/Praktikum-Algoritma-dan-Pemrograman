#!/usr/bin/python
# Mengakses data / objek biner dengan shelve

import shelve
f = open('L200180149', 'r')
NIM = f.readline()
TL = f.readline()
Nama = f.readline()
f.close()

f = shelve.open("Fauzi")
f['b'] = [NIM, TL, Nama]
print f['b'][0]
print f['b'][1]
print f['b'][2]
f.close()
