import socket
import threading

# Define the server address and port
server_address = ('localhost', 8000)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Bank server is running...")

# Function to handle a single client connection
def handle_client(client_socket):
    # initial account balance
    account_balance = 1000
    try:
     while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode().lower()

        if not data:
            break

        if data == "balance":
            response = f"Your balance is RS.{account_balance}"
        elif data.startswith("withdraw "):
            try:
                amount = float(data.split()[1])
                if amount > 0 and amount <= account_balance:
                    account_balance -= amount
                    response = f"Withdrawn {amount}. Your new balance is {account_balance}"
                else:
                    response = "Invalid withdrawal amount"
            except ValueError:
                response = "Invalid withdrawal request"
        elif data.startswith("deposit "):
            try:
                amount = float(data.split()[1])
                if amount > 0:
                    account_balance += amount
                    response = f"Deposited {amount}. Your new balance is {account_balance}"
                else:
                    response = "Invalid deposit amount"
            except ValueError:
                response = "Invalid deposit request"
        else:
            response = "Invalid request"

        client_socket.send(response.encode())
    except ConnectionResetError:
        pass
    finally:
        client_socket.close()

thread_pool=[]

while True:
    # Wait for a client to connect
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    if(len(thread_pool)<=5):
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
        thread_pool.append(client_handler)
    else:
        print("Server reached its limit")
    while len(thread_pool) >= 5:
        for thread in thread_pool:
            if not thread.is_alive():
                thread_pool.remove(thread)
                print(f"Connection terminated from{client_address}")
                break
