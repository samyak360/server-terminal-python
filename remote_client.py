#!/usr/bin/env python2

import  socket,commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.1.37"
port=7890
port2=7892

#  binind ip and port with bind function that takes input as tuple
s.bind(("",port2))

# defining list for 10 commands counter
timer=[]
while  True :
#  sending  data to  target machine 
	cmd=raw_input("samyak@sam:~$ ")
	s.sendto(cmd,(ip,port))
	if  'exit' in  cmd  or  'close' in cmd:
		print "closing server.."
		exit()
	else :
		timer.append(cmd)
		if  len(timer) > 5 :
			print commands.getoutput('clear')
			for i in  range(len(timer)):
				timer.pop()
		server_data=s.recvfrom(100)
                #   only  server  data is stored and printed
	        recv_cmd=server_data[0]
		print recv_cmd

s.close()

