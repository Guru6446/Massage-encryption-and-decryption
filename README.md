Step 1: Understanding the Purpose
This Python program implements a Caesar Cipher, a simple encryption technique where each letter in the text is shifted by a fixed number of places in the alphabet.
The user can choose to either encrypt or decrypt a message.
Step 2: Function Definitions
The program contains two main functions:

1. encrypt(text, shift)
Takes the input text and shifts each letter forward by shift positions in the alphabet.
Handles both uppercase and lowercase letters separately.
Leaves non-alphabetic characters (like spaces, numbers, and punctuation) unchanged.
2. decrypt(encrypted_text, shift)
Similar to encryption but shifts each letter backward by shift positions to restore the original message.
Step 3: Main Program Execution
The main() function is responsible for handling user input and running the encryption or decryption process.

Ask the user for a choice

"e" for encryption
"d" for decryption
If the user chooses encryption ('e'):

Ask for the text to encrypt.
Ask for the shift value (number of positions to shift).
Call encrypt(text, shift).
Print the encrypted message.
If the user chooses decryption ('d'):

Ask for the encrypted text.
Ask for the shift value.
Call decrypt(encrypted_text, shift).
Print the decrypted message.
If the user enters an invalid choice:

Print "Invalid choice".
Step 4: Running the Program
The script executes main() when run directly (if __name__ == "__main__":).
The program waits for user input and processes it accordingly.
Example Walkthrough
Encryption Example
rust
Copy
Edit
Enter 'e' for encryption or 'd' for decryption: e
Enter the message to encrypt: Hello World
Enter the shift value: 3
'H' → 'K', 'e' → 'h', 'l' → 'o', 'o' → 'r', 'W' → 'Z', etc.
pgsql
Copy
Edit
Encrypted message: Khoor Zruog
Decryption Example
rust
Copy
Edit
Enter 'e' for encryption or 'd' for decryption: d
Enter the message to decrypt: Khoor Zruog
Enter the shift value: 3
'K' → 'H', 'h' → 'e', 'o' → 'l', etc.
yaml
Copy
Edit
Decrypted message: Hello World
Step 5: Summary of Logic
Character shifting is done using ASCII values (ord() and chr()).
Modulo (% 26) ensures the shift wraps around the alphabet.
Input validation is minimal (assumes valid integer shift input).
