import socket
# server address and port
server_address = ('localhost',8000)

# Create  TCP connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to  server
client_socket.connect(server_address)


while True:
    # Get user input
    request = input("Enter 'balance', 'withdraw <amount>', 'deposit <amount>', or 'exit': ")
    
    if request.lower() == 'exit':
        break
    
    # Send the request to the server
    client_socket.send(request.encode())
    
    # Receive and print the server's response
    response = client_socket.recv(1024).decode()
    print("Server response:", response)

# Close the socket
client_socket.close()
