import socket
import time
import sys


localIP     = socket.gethostbyname(socket.gethostname())
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
#while(True):
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
print(clientMsg)
print(clientIP)

for i in range(100):
    # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
        time.sleep(0.1)
        print(address)
