from socket import *
from random import *
import sys
import select

host = "0.0.0.0"
port = 5454

s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

#get user input for
receiver = input("what is the IP of the receiver: ")
drop_rate = float(input(" what is the drop rate: "))

addr = (host, port)
buf = 1024
print("listening")
data, addr = s.recvfrom(buf)
send_addr = addr
print("data received", data)

while(data):

        print("data received")
        if(data):
            if(addr == send_addr):
                num = random()
                if(num > drop_rate):
                    r = socket(AF_INET, SOCK_DGRAM)  # creates socket
                    host = receiver # hostname to send file to
                    port = 5454
                    buf = 1024
                    addr = (host, port)
                    print("sending to", host)
                    r.sendto(data, addr)  # sends file name to receiver to allocate space for writing data
            else:
                num = random()
                if (num > drop_rate):
                    r = socket(AF_INET, SOCK_DGRAM)  # creates socket
                    host = send_addr  # hostname to send file to
                    port = 5454
                    buf = 1024
                    addr = (host, port)
                    print("sending to", host)
                    r.sendto(data, addr)  # sends file name to receiver to allocate space for writing data

        s.settimeout(None)
        data, addr = s.recvfrom(buf)
        print("received more data: ", data)

s.close()
