def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = [x for x in plaintext]
    for i in range(len(ciphertext)):
        if  65 <= ord(ciphertext[i]) <= 90 - shift:
            ciphertext[i] = chr(ord(ciphertext[i]) + shift)
        elif 90 - shift <= ord(ciphertext[i]) <= 90:
            ciphertext[i] = chr(65 + abs(90 - (ord(ciphertext[i]) + shift)) - 1)
        if  97 <= ord(ciphertext[i]) <= 122 - shift:
            ciphertext[i] = chr(ord(ciphertext[i]) + shift)
        elif 122 - shift <= ord(ciphertext[i]) <= 122:
            ciphertext[i] = chr(97 + abs(122 - (ord(ciphertext[i]) + shift)) - 1)

    ciphertext = "".join(ciphertext)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = [x for x in ciphertext]
    for i in range(len(plaintext)):
        if 65 + shift <= ord(plaintext[i]) <= 90:
            plaintext[i] = chr(ord(plaintext[i]) - shift)
        elif 65 <= ord(plaintext[i]) <= 65 + shift:
            plaintext[i] = chr(90 - abs(65 - (ord(plaintext[i]) - shift)) + 1)
        if 97 + shift <= ord(plaintext[i]) <= 122:
            plaintext[i] = chr(ord(plaintext[i]) - shift)
        elif 97 <= ord(plaintext[i]) <= 97 + shift:
            plaintext[i] = chr(122 - abs(97 - (ord(plaintext[i]) - shift)) + 1)


    plaintext = "".join(plaintext)
    return plaintext