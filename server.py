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
from socket import *

#We only need one input parameter
NUM_INPUTS = 1

def input_verify(args):
	if len(args) != NUM_INPUTS:
		print("Wrong number of input")
		exit(1)
	try:
		req_code = int(args[0])

	except:
		print("Wrong format of arguments")
		exit(1)
	return


#carries out TCP functionality on server side
def TCP_handshaking(req_code):
    #create TCP scocket
    serverTCPSocket = socket(AF_INET,SOCK_STREAM)
    serverTCPSocket.bind(('',0))
    serverTCPSocket.listen(1)
    serverTCPHost, n_port = serverTCPSocket.getsockname()
    serverUDPSocket = socket(AF_INET, SOCK_DGRAM)
    serverUDPSocket.bind(('',0))
    serverUDPHost, r_port = serverUDPSocket.getsockname()
    
    print("SERVER_PORT = ", str(n_port))
    
    while True:
        #receive req_code from client
        connectionSocket,addr = serverTCPSocket.accept()
        receive_code = connectionSocket.recv(1024)
        #check if the received code is correct
        if receive_code.decode() == str(req_code):
            #send the r_port to client
            connectionSocket.send(str(r_port).encode())
            break
        else: #code is incorrect, exit
            serverTCPSocket.close()
            exit(1)
    connectionSocket.close()
    return serverUDPSocket
        
#carries out UDP transfer functionality from server side
def UDP_transfer(serverUDPSocket) :
    #create UDP socket first
    while True:
        msg,clientAddress = serverUDPSocket.recvfrom(2048)
        reversedmsg = msg[::-1]
        serverUDPSocket.sendto(reversedmsg.encode(),clientAddress)
        break
    serverUDPSocket.close()

def main():
    input_verify(sys.argv[1:])
    req_code = sys.argv[1]

	#handshaking
    UDPsocket = TCP_handshaking(req_code)

	#UDP_Transfer
    UDP_transfer(UDPsocket)

main()
