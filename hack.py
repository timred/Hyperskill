import argparse
import socket

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("hostname", type=str)
parser.add_argument("port", type=int)
parser.add_argument("message", type=str)
args = parser.parse_args()

# Connect
address = (args.hostname, args.port)
client_socket = socket.socket()
client_socket.connect(address)

# Send & Receive Data
client_socket.send(args.message.encode())
response = client_socket.recv(1024)
response = response.decode()
print(response)
