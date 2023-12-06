# UDPPingerServer.py
# We will need the following modules to generate randomized lost packets import random
import socket
from socket import AF_INET, SOCK_DGRAM
import random

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
# Assign IP address and port number to socket
serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((socket.gethostbyname(socket.gethostname()), 12000))
print('Server ready to receive')
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue

    # Otherwise, the server responds
    print(f'Received: {message.decode('utf-8')}')
    serverSocket.sendto(message, address)
