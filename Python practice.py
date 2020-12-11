import socket,struct
import os
from pythonping import ping


def check_if_ip_up_or_down(ip):
    stream = os.popen(f"ping {ip}")
    # read a stream
    read = stream.read()
    print(read)

    # split a output
    output = read.split("\n")

    # split index wise 
    # line = output[1].split(" ")

    # # check if bits are receive or not 
    # if line[3] != None:
    #     print("success with :", ip)
    # else:
    #     print("Fail")    
    bytes_occurance=0
    for line in output:
        if line.find("bytes=") < 0:
            None
        else:
            bytes_occurance=bytes_occurance+1

    # print(bytes_occurance)
    if bytes_occurance <1:
        print("Host is Down")
    else:
        print("Host is UP")    

# hostname = socket.gethostname()
# myip = socket.gethostbyname(hostname)

# print("this is host name :",hostname)
# print("this is Zek Ip :", myip)
ip_address = "10.0.1.169"

check_if_ip_up_or_down(ip_address)
