def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The message to encrypt or decrypt
        shift (int): The number of positions to shift the letters
        mode (str): 'encrypt' to encrypt, 'decrypt', to decrypt.
    
    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char_code = (ord(char) - start + shift) % 26
            if mode == 'decrypt':
                shifted_char_code = (ord(char) - start - shift + 26) % 26
            result += chr(start + shifted_char_code)
        else:
            result += char
    return result

# Allow the user to input their own message
message = input("Enter the message to encrypt/decrypt: ")

# Allow the user to input their own key, with basic error handling
while True:
    try:
        key_input = input("Enter the shift key (an integer): ")
        key = int(key_input)
        break
    except ValueError:
        print("Invalid input. Please enter an integer for the shift key.")

# Encrypt the user's message
encrypted_message = caesar_cipher(message, key, 'encrypt')
print(f"Original: {message}")
print(f"Encrypted: {encrypted_message}")

# Decrypt the encrypted message
decrypted_message = caesar_cipher(encrypted_message, key, 'decrypt')
print(f"Decrypted: {decrypted_message}")
