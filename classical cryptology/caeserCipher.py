"""
Author: Rohan Singh
Python code for Caeser Cypher
"""


# This function computes all of the possible meanings for a given cipher text using 26 alphabet shifts
def caesar_cipher(text):
    for shift in range(26):
        decrypted_text = ''
        for char in text:
            if char.isalpha():
                if char.islower():
                    decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += char
        print(f"Shift {shift}: {decrypted_text}")



# Main function
def main():
    cipher_text = "LWKLQNWKDWLVKDOOQHYHUVHHDELOOERDUGORYHOBDVDWUHH"
    caesar_cipher(cipher_text)



if __name__ == "__main__":
    main()