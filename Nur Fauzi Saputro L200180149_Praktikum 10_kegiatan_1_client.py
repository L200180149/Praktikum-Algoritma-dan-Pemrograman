# nama berkas : p_tcpcli.py
# client TCP untuk serber p_tcpser.py
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50006))
print('Mesin chat sudah siap')
while pesan.lower() != 'q':
    pesan = raw_input('Tanyakan : ', )
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print "Jawaban : ", response
    else:
        print 'Bayyy'
s.close
