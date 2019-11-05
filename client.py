#CS456 Assignment1
#Editor:Boyan Zhou
#
#four input parametera
#1.<server_address>
#2.<n_port>
#3.<req_code>
#4.<msg>

#import libabries
import sys
import time
from socket import *

#we must have four input parameters
num_input = 4

#check if the number and the type of input
def input_verify(args):
    if len(args) != num_input:
        print("Wrong number of input")
        exit(1)
    try:
        server_address = args[0]
        n_port = args[1]
        req_code = args[2]
        msg = args[3]

        if not server_address or not n_port or not req_code or not msg:
            raise error
    
    except error:
        print("Invalid empty string")
        exit(1)
    except:
        print("Wrong format of arguments")
        exit(1)
    return

#carries out TCP handshaking functionality on client side
def TCP_handshaking(req_code,server_address,n_port):
    #create TCP socket
    clientTCPSocket = socket(AF_INET,SOCK_STREAM)

    #send request code to server
    while True:
        #send req_code to server
        clientTCPSocket.connect((server_address,n_port))
        clientTCPSocket.send(str(req_code).encode())
        
        #receive r_port from server
        r_port = clientTCPSocket.recv(1024)
        if (str(r_port) == ""):
            print("Unexpected r_port value received")
            exit(1)
        else:
            break
    clientTCPSocket.close()
    return r_port

#carries out UDP functionality from client side
def UDP_Transfer(msg,server_address,r_port):
    #create UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(msg.encode(),(server_address,int(r_port)))
    #get reversed message from server
    reverseMsg,serveradd = clientSocket.recvfrom(2048)
    print('Client reverse message is: '+ reverseMsg)
    clientSocket.close()

def main():
    input_verify(sys.argv[1:])
    server_address = sys.argv[1]
    n_port = int(sys.argv[2])
    req_code = int(sys.argv[3])
    msg = sys.argv[4]

    #handshaking
    r_port = TCP_handshaking(req_code,server_address,n_port)
    
    #UDP transfer
    UDP_Transfer(msg,server_address,r_port)

    exit(0)

main()

