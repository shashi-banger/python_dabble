import socket
import sys

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = (sys.argv[1], int(sys.argv[2]))
bufferSize          = 1024


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
print(serverAddressPort)
ret=UDPClientSocket.sendto(bytesToSend, serverAddressPort)
print(ret)

for i in range(100):
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
