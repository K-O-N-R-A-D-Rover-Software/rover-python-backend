import socket
import sys

IP = "127.0.0.1" 
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"Listening for clients at {(IP, PORT)}")

while True:
    data, address = sock.recvfrom(4096)

    print(f"Received {data} from {address}")
    #message = input("Reply? ")
    #sock.sendto(message.encode(), address)