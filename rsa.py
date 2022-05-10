#prompt the user to choose either encryption (e) or decryption (d)
#prompt the user for two prime numbers p and q and an encryption exponent e
#prompt the user to input a numerical plaintext message
#display decryption exponent d and the Euler's toitient number


import math
import random
import sys


def main():
    print("Welcome to the RSA encryption program!")
    print("Please choose either encryption (e) or decryption (d)")
    choice = input()
    if choice == "e":
        encryption()
    elif choice == "d":
        decryption()
    else:
        print("Invalid input")
        sys.exit()


def encryption():
    print("Please enter two prime numbers p and q")
    p = int(input())
    q = int(input())
    print("Please enter an encryption exponent e")
    e = int(input())
    print("Please enter a numerical plaintext message")
    m = int(input())
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    c = pow(m, e) % n
    print("The encryption exponent is:", e)
    print("The decryption exponent is:", d)
    print("The Euler's toitient number is:", phi)
    print("The ciphertext is:", c)


def decryption():
    print("Please enter two prime numbers p and q")
    p = int(input())
    q = int(input())
    print("Please enter an encryption exponent e")
    e = int(input())
    print("Please enter a numerical ciphertext")
    c = int(input())
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    m = pow(c, d) % n
    print("The decryption exponent is:", d)
    print("The Euler's toitient number is:", phi)
    print("The plaintext is:", m)


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

main()


