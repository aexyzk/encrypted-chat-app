import socket
import threading
import sys

import random, string

# encyption

chars = " " + string.punctuation + string.digits + string.ascii_letters + "üäöß"
chars = list(chars)

def new_key():
    key = chars.copy()
    random.shuffle(key)
    print(key)

key = ['j', ')', '|', 'd', 'I', '$', ';', 'y', ' ', 'H', 'x', '~', '.', 'N', 'm', ']', '3', 'n', '`', 'g', '-', 'ä', 'l', '@', 'D', 'q', '4', 'M', ',', '5', 'R', '#', 'A', 'S', 'z', '1', ':', '?', 'Z', '[', 'E', 'b', 'h', 'v', 'J', 'o', '0', '{', 'O', 'i', 't', 'f', 'r', '(', 'F', 'K', 'ß', 'a', 'ö', '}', '>', '_', 'G', 
'W', 'Q', 'B', '^', 'k', 'U', '%', '+', '&', "'", '"', 'V', 'p', '*', '2', 'u', '<', '7', '8', 'L', 'X', '6', 's', 'c', 'e', 'w', '9', 'C', '=', 'ü', '!', 'Y', 'P', 'T', '/', '\\']

print(key)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    server_address = ('172.22.106.223', 12345)
    client_socket.connect(server_address)
except:
    print("Error: Couldn't Connect To Server: E001: Check with the admin to make sure the server is up!")
    sys.exit()
else:
    pass

print("*** genaric e2e encrypted chat app ***{:^}".format)

def username():
    global uname
    uname = input("username: ")
    if len(uname) < 2:
        print("Error: Username Error: E002: Your Username is too short!")
        username()
    elif len(uname) > 20:
        print("Error: Username Error: E003: Your Username is too long!")
        username()

# Send messages to the server
def send_message():
    while True:
        # Input message from the client
        message = input("")
        message = (f"{uname}: {message}")

        #ecrypt

        plain_text = message
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        #send
        client_socket.send(cipher_text.encode())

# Receive messages from the server
def receive_message():
    while True:
        # Receive messages from the server
        message = client_socket.recv(1024).decode()

        #decrypt

        cipher_text = message
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(plain_text)

username()

# Start sending and receiving messages in separate threads
threading.Thread(target=send_message).start()
threading.Thread(target=receive_message).start()