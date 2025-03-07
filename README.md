Encryption-Decryption Script
This Python script allows you to encrypt or decrypt a message using a simple shift cipher. It supports letters (a-z), some special characters (*, @, !), and numbers (1-9).

Features
Encrypts messages by shifting characters forward.
Decrypts messages by shifting characters backward.
Supports spaces in messages.
Provides a simple CLI interface for user input.
How to Use
Clone this repository or copy the script.
Run the script in a Python environment.
Follow the on-screen instructions:
Type 'encode' to encrypt a message.
Type 'decode' to decrypt a message.
Enter your message.
Enter the shift number.
The script will output the encrypted or decrypted message.
Example Usage
bash
Copy code
TYpe 'encode' to encrypt, type 'decode' to decrypt:
encode
TYpe your message:
hello
TYpe the shift number:
3
khoor  # Output
bash
Copy code
TYpe 'encode' to encrypt, type 'decode' to decrypt:
decode
TYpe your message:
khoor
TYpe the shift number:
3
hello  # Output
Notes
Ensure that all characters in the message exist in the alphabet list.
The shift number should be a valid integer.
The script currently does not handle cases where the shift moves beyond the available characters.
Improvements Needed
Add error handling for out-of-range shifts.
Improve handling for characters not in the alphabet list.
Allow user-defined alphabets.
License
This project is open-source and free to use. Contributions are welcome!






