# Bastic Encryption Models

In thit project we have created a simple neon/cyberpunk page to test out some common encryption models, those being Caesar Cipher, RSA public/privat key and Hashin

The page uses flask to create a simple user-face for demonstation

## Caesar Cipher

  The Caesar cipher is one of the simplest and oldest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, A → D, B → E, C → F, and so on. When the end of the alphabet is reached, it wraps around (e.g., X → A).

It’s easy to implement but also easy to break, since there are only 25 possible shifts. Modern cryptography considers it insecure, but it’s useful for teaching basic encryption concepts.

## RSA Public/Private key

  RSA is a widely used asymmetric cryptosystem, meaning it uses two different keys:

Public key: shared with everyone; used to encrypt data.

Private key: kept secret; used to decrypt data.

The security of RSA comes from the difficulty of factoring very large composite numbers (products of two primes). When someone encrypts a message using your public key, only your private key can decrypt it. RSA is used in HTTPS, digital signatures, and secure key exchange.

## Hashing (SHA256)

  SHA-256 is a cryptographic hash function that takes any input and produces a fixed 256-bit (64-character) hash.

Key properties:

One-way: you cannot reverse a hash to recover the original input.

Deterministic: the same input always produces the same hash.

Collision-resistant: extremely hard for two different inputs to produce the same hash.

Avalanche effect: small input changes cause large, unpredictable changes in the output.

SHA-256 is widely used for password hashing (with added salt), file integrity checks, digital signatures, and blockchain systems like Bitcoin.
