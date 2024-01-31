"""
Python Code for Affine Cipher
Author: Rohan Singh
"""



# helper function for modulo inverse (which is required for affine cipher decryption)
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None



# function to encrypt a message given the keys and prime p
def encrypt_affine(m, k1, k2, p):
    return (k1 * m + k2) % p



# function to decrypt the ciphertext given the keys and prime p
def decrypt_affine(c, k1, k2, p):
    k1_inv = mod_inverse(k1, p)
    return (k1_inv * (c - k2)) % p



# main function
def main():

    p = 541
    k = (34, 71)
    m = 204
    c = 431

    encrypted_message = encrypt_affine(m, k[0], k[1], p)


    decrypted_ciphertext = decrypt_affine(c, k[0], k[1], p)

    print(f"The Encrypted Message for {m} is : {encrypted_message}")
    print(f"Decrypted Ciphertext for {c} is: {decrypted_ciphertext}")


    print("\nTesting correctness of affine cipher:")


    p1 = 1373
    k1 = (13, 29)
    m1 = 307

    encrypted_message1 = encrypt_affine(m1, k1[0], k1[1], p1)

    decrypted_ciphertext1 = decrypt_affine(encrypted_message1, k1[0], k1[1], p1)

    print(f"The Encrypted Message for {m1} is : {encrypted_message1}")
    print(f"Decrypted Ciphertext for {encrypted_message1} is: {decrypted_ciphertext1}")




if __name__ == "__main__":
    main()