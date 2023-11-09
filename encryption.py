import random, string

chars = " " + string.punctuation + string.digits + string.ascii_letters + "üäöß"
chars = list(chars)

def new_key():
    key = chars.copy()
    random.shuffle(key)
    print(key)

key = ['j', ')', '|', 'd', 'I', '$', ';', 'y', ' ', 'H', 'x', '~', '.', 'N', 'm', ']', '3', 'n', '`', 'g', '-', 'ä', 'l', '@', 'D', 'q', '4', 'M', ',', '5', 'R', '#', 'A', 'S', 'z', '1', ':', '?', 'Z', '[', 'E', 'b', 'h', 'v', 'J', 'o', '0', '{', 'O', 'i', 't', 'f', 'r', '(', 'F', 'K', 'ß', 'a', 'ö', '}', '>', '_', 'G', 
'W', 'Q', 'B', '^', 'k', 'U', '%', '+', '&', "'", '"', 'V', 'p', '*', '2', 'u', '<', '7', '8', 'L', 'X', '6', 's', 'c', 'e', 'w', '9', 'C', '=', 'ü', '!', 'Y', 'P', 'T', '/', '\\']

print(key)

#ecrypt

plain_text = input("Enter a message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(cipher_text)

#decrypt

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(plain_text)