def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text
# banner
banner = """
_____          ______  _____         _____     _____ _____ _____  _    _ ______ _____  
  / ____|   /\   |  ____|/ ____|  /\   |  __ \   / ____|_   _|  __ \| |  | |  ____|  __ \ 
 | |       /  \  | |__  | (___   /  \  | |__) | | |      | | | |__) | |__| | |__  | |__) |
 | |      / /\ \ |  __|  \___ \ / /\ \ |  _  /  | |      | | |  ___/|  __  |  __| |  _  / 
 | |____ / ____ \| |____ ____) / ____ \| | \ \  | |____ _| |_| |    | |  | | |____| | \ \ 
  \_____/_/    \_\______|_____/_/    \_\_|  \_\  \_____|_____|_|    |_|  |_|______|_|  \_\
                                                                                          
"""
print(banner)
# Taking user input
plaintext = input("Enter the text to be encrypted: ")
shift = int(input("Enter the shift value: "))

# Encrypting and decrypting using user inputs
encrypted = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
