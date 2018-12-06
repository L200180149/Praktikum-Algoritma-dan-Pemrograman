# Nama berkas : p_tcpser.py
# TCP server untuk client p_tcpcli.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print "Server sudah siap broo!!"
data = ''
kamus = {'nama' : 'Nur Fauzi Saputro' ,
         'umur' : 'saya lebih muda dari anda' ,
         'nim' : 'L200180149' ,
         'motto' : 'Sudahilah cheaty-chat-chat' ,
         'kuliah' : 'Informatika UMS'}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'Q' and data != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'Pertanyaan anda: ' , data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Pertanyaan anda tida relevan')
