import socket
import time

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 500)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("........SERVER.........")
print("Waiting for connection ....")

# Accept a connection
connection, client_address = server_socket.accept()

try:
    print("Received request for sending frames")
    p = connection.recv(1)[0]
    pc = connection.recv(1)[0]
    
    print("Sending......")
    if pc == 0:  # No error case
        for i in range(p):
            print(f"Sending frame number {i}")
            connection.sendall(bytes([i]))
            print("Waiting for acknowledgment")
            time.sleep(7)  # Simulate delay
            a = connection.recv(1)[0]
            print(f"Received acknowledgment for frame {i} as {a}")
    else:  # Error case
        f = [False] * p
        for i in range(p):
            if i == 2:
                print(f"Sending frame number {i}")
            else:
                print(f"Sending frame number {i}")
                connection.sendall(bytes([i]))
                print("Waiting for acknowledgment")
                time.sleep(7)  # Simulate delay
                a = connection.recv(1)[0]
                if a != 255:
                    print(f"Received acknowledgment for frame {i} as {a}")
                    f[i] = True
        
        # Resend frames that were not acknowledged correctly
        for a in range(p):
            if not f[a]:
                print(f"Resending frame number {a}")
                connection.sendall(bytes([a]))
                print("Waiting for acknowledgment")
                time.sleep(5)  # Simulate delay
                b = connection.recv(1)[0]
                print(f"Received acknowledgment for frame {a} as {b}")
                f[a] = True

finally:
    print("Closing connection")
    connection.close()
    server_socket.close()

