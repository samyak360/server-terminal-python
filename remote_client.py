#!/usr/bin/env python2

import  socket,commands,subprocess
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.1.38"
port=7890
#defining functions for windows and linux servers
def linux():
	# defining list for dangerous commands
	dangerous_cmd=['shutdown','reboot','halt','poweroff','rm',':(){:|:&};:','> /dev/sda','mkfs.ext3 /dev/sda','/dev/sda']
        # defining list for 5 commands counter
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
                        if "sh: 1" in recv_cmd :
                                print "\ncommand not found..\nmake sure you are connected to LINUX server\n"
                        else:
                                print "\n",recv_cmd,"\n"

def windows():
        # defining list for 10 commands counter
        timer=[]
        while  True :
        #  sending  data to  target machine 
                cmd=raw_input("G:\projectpython\server-terminal-python> ")
                s.sendto(cmd,(ip,port))
                if  'exit' in  cmd  or  'close' in cmd:
                        print "closing server.."
                        exit()
                else :
                        timer.append(cmd)
                        if  len(timer) > 5 :
                                subprocess.call('cls',shell=True)
                                for i in  range(len(timer)):
                                        timer.pop()
                        server_data=s.recvfrom(500)
                        #   only  server  data is stored and printed
                        recv_cmd=server_data[0]
                        if "not recognized" in recv_cmd :
                                print "\ncommand not found..\nmake sure you are connected to WINDOWS server\n"
                        else:
                                print "\n",recv_cmd,"\n"                                
#authentication from server
user = raw_input("enter your username: ")
password = raw_input("enter your password: ")
s.sendto(user,(ip,port))
s.sendto(password,(ip,port))
msg = s.recvfrom(40)
if msg[0] == 'ok' :
        os = subprocess.check_output('nmap -O -V 192.168.1.37',shell=True)
        if 'windows' in os:
                windows()
        else:
                linux()
else:
        print "\n",msg[0]
s.close()


