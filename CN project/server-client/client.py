import socket
import time

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 500)
print("........CLIENT.........")
print("Connecting to server...")
client_socket.connect(server_address)

try:
    # Send the number of frames to the server
    c = int(input("Enter the number of frames to be requested from the server: "))
    client_socket.sendall(bytes([c]))

    # Send the type of transmission (Error = 1, No Error = 0)
    choice = int(input("Enter the type of trans. Error=1; No Error=0: "))
    client_socket.sendall(bytes([choice]))

    check = 0

    if choice == 0:
        # No error case
        for j in range(c):
            i = client_socket.recv(1)[0]
            print(f"Received frame number: {i}")
            print(f"Sending acknowledgment for frame number: {i}")
            client_socket.sendall(bytes([i]))
    else:
        # Error case
        for j in range(c):
            i = client_socket.recv(1)[0]
            if i == check:
                print(f"Received frame number: {i}")
                client_socket.sendall(bytes([i]))
                check += 1
            else:
                print(f"Discarded frame number: {i}")
                print("Sending negative acknowledgment")
                client_socket.sendall(bytes([-1]))

finally:
    print("Closing connection")
    client_socket.close()
