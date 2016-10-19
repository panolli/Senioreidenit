import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(10)

while (1):
    sc, address = s.accept()
    print address
    f = open(str(address) + '_' + ".txt",'wb') #jos ei toimi korvaa adress 'file_'stringilla
    while (True):
	#luetaan dataa ja tallentetaan txt muotoon(jatkossa json)
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    sc.close()

s.close()
