def encrypt_vigenere(plaintext, key):
    result = ""
    key = key.upper()
    plaintext = plaintext.upper()

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result


def decrypt_vigenere(ciphertext, key):
    result = ""
    key = key.upper()
    ciphertext = ciphertext.upper()
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result
