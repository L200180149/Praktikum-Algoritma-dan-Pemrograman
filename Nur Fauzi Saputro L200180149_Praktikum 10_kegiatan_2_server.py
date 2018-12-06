import socket
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print "Server sudah siap broo!!"
data = ''

while data.lower() != 'quit':
    komm, addr = s.accept()
    while data.lower() != 'quit':
        data = komm.recv(1024)
        if data.lower() == 'quit':
            s.close()
            break
        print 'Command : ' , data
        if data.lower() == 'machine':
            a = platform.machine()
            komm.send(a)
        if data.lower() == 'release':
            b = platform.release()
            komm.send(b)
        elif data.lower() == 'system':
            c = platform.system()
            komm.send(c)
        elif data.lower() == 'version':
            d = platform.version()
            komm.send(d)
        elif data.lower() == 'node':
            e = platform.node()
            komm.send(e)
        else:
            komm.send('Unknown Command')
