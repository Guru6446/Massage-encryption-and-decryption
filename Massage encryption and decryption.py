def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Enter 'e' for encryption or 'd' for decryption: ")
    if choice.lower() == 'e':
        text = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = encrypt(text, shift)
        print("Encrypted message:", encrypted_text)
    elif choice.lower() == 'd':
        encrypted_text = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = decrypt(encrypted_text, shift)
        print("Decrypted message:", decrypted_text)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


