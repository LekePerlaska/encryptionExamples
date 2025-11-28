from hashlib import sha256

def hashing(hash):
    return sha256(hash.encode('utf-8')).hexdigest()

def caesarCipherEncrypt(plainText, key):
    cipher = ""
    for c in plainText:
        if c.isalpha():
            if c.isupper():
                cipher += chr(((ord(c) - ord('A') + key) % 26) + ord('A'))
            else:
                cipher += chr(((ord(c) - ord('a') + key) % 26) + ord('a'))
        else:
            cipher += c
    return cipher

def caesarCipherDecrypt(cipher, key):
    return caesarCipherEncrypt(cipher, 26-key)

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generateKeys():
    p = 7919
    q = 1009
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)

    return e, d, n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encryptRSA(m, e, n):
    ascii_values = [ord(c) for c in m]
    cipher = []
    for i in ascii_values:
        cipher.append(power(i, e, n))
    
    formated = ""
    for i in cipher:
        formated += f" {i}"
    return formated

def decryptRSA(c, d, n):
    message = ""
    for i in c.split(" "):
        message += chr(power(int(i), d, n))
    return message


def main():
    CE = caesarCipherEncrypt("Hello!", 3)
    CD = caesarCipherDecrypt("Khoor!", 3)

    print(hashing("Howdi!"))

    print(f"Caesar Cipher Encrypted: {CE}")
    print(f"Caesar Cipher Decrypted: {CD}")

    e, d, n = generateKeys()

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    M = "Hello There!"
    print(f"Original Message: {M}")

    C = encryptRSA(M, e, n)
    print(f"Encrypted Message: {C}")

    decrypted = decryptRSA(C, d, n)
    print(f"Decrypted Message: {decrypted}")


if __name__ == "__main__":
    main()
