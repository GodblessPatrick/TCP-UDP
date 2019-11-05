# TCP-UDP
Implement a client program (client) and a server program (server) to communicate between
themselves.

## 1.summary
the client will send requests to the server to reverse strings (taken as a command
line input) over the network using sockets.
This program uses a two stage communication process. In the negotiation stage, the client and the
server negotiate on a random port (<r_port>) for later use through a fixed negotiation port (<n_port>)
of the server. Later in the transaction stage, the client connects to the server through the selected
random port for actual data transfer.

## 2.Signalling
The signalling in this project is done in two stages as shown in Figure 2.  
**Stage 1.** Negotiation using TCP sockets: In this stage, the client creates a TCP connection with the server
using <server_address> as the server address and <n_port> as the negotiation port on the server
(where the server is listening). The client sends a request to get the random port number from the
server where it will send the actual request (i.e., the string to be reversed). To initiate this negotiation,
the client sends a request code (<req_code>), an integer (e.g., 13), after creating the TCP connection.
If the client fails to send the intended <req_code>, the server closes the TCP connection.
Once the server verifies the <req_code>, it replies back with a random port number
<r_port> where it will be listening for the actual request. After receiving this <r_port>,
the client closes the TCP connection with the server.  
**Stage 2**. Transaction using UDP sockets: In this stage, the client creates a UDP socket to the server in
<r_port> and sends the <msg> containing a string. On the other side, the server receives the string
and sends the reversed string back to the client. Once received, the client prints out the reversed string
and exits. Note that the server should continue listening on its <n_port> for subsequent client requests.
For simplicity, we assume, there will be only one client in the system at a time. So, the server does not
need to handle simultaneous client connections.

## 3.Usage
Run server: ./server.sh <req_code> 

Run client: ./client.sh <server address> <n_port> <req_code> 'A man, a plan, a canal—
Panama!'
