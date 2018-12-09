## Program menghitung luas permukaan prisma
## Bagian server

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print "Server sudah siap"
perintah = ''
a=0

while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'alassegitiga':
                a = int(data[1])
                respon = "alas segitiga dicatat"
                komm.send(respon)
            elif perintah == 'tinggisegitiga':
                b = int(data[1])
                respon = "tinggi segitiga dicatat"
                komm.send(respon)
            elif perintah == 'tinggiprisma':
                c = int(data[1])
                respon = "tinggi prisma dicatat"
                komm.send(respon)
            
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = (0.5*a*b)*c
            respon = "Luas persegi dengan alas segitiga {}, tinggi segitiga {}, alas prisma {} adalah {}".format(a,b,c,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
