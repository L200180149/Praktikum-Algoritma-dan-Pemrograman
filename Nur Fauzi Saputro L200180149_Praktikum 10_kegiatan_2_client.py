import socket
import platform

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50006))
print('Mesin chat sudah siap')
while pesan.lower() != 'quit':
    pesan = raw_input('Command : ', )
    s.send(pesan)
    if pesan.lower() != 'qui':
        response = s.recv(1024)
        print "Response : ", response
    else:
        print 'Bayyy'
s.close
