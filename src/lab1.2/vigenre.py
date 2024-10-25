def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = [x for x in plaintext]
    keyword = keyword.upper()
    keyword = [x for x in keyword]

    if len(keyword) > len(ciphertext):
        keyword = keyword[: len(ciphertext)]

    while len(keyword) < len(ciphertext):
        keyword += keyword
        if len(keyword) > len(ciphertext):
            keyword = keyword[: len(ciphertext)]

    for i in range(len(ciphertext)):
        if  65 <= ord(ciphertext[i]) <= 90 - (ord(keyword[i]) - 65):
            ciphertext[i] = chr(ord(ciphertext[i]) + (ord(keyword[i]) - 65))
        elif 90 - (ord(keyword[i]) - 65) <= ord(ciphertext[i]) <= 90:
            ciphertext[i] = chr(65 + abs(90 - (ord(ciphertext[i]) + (ord(keyword[i]) - 65))) - 1)
        if  97 <= ord(ciphertext[i]) <= 122 - (ord(keyword[i]) - 65):
            ciphertext[i] = chr(ord(ciphertext[i]) + (ord(keyword[i]) - 65))
        elif 122 - (ord(keyword[i]) - 65) <= ord(ciphertext[i]) <= 122:
            ciphertext[i] = chr(97 + abs(122 - (ord(ciphertext[i]) + (ord(keyword[i]) - 65))) - 1)

    ciphertext = "".join(ciphertext)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = [x for x in ciphertext]
    keyword = keyword.upper()
    keyword = [x for x in keyword]

    if len(keyword) > len(ciphertext):
        keyword = keyword[: len(ciphertext)]

    while len(keyword) < len(ciphertext):
        keyword += keyword
        if len(keyword) > len(ciphertext):
            keyword = keyword[: len(ciphertext)]

    for i in range(len(plaintext)):
        if 65 + (ord(keyword[i]) - 65) <= ord(plaintext[i]) <= 90:
            plaintext[i] = chr(ord(plaintext[i]) - (ord(keyword[i]) - 65))
        elif 65 <= ord(plaintext[i]) <= 65 + (ord(keyword[i]) - 65):
            plaintext[i] = chr(90 - abs(65 - (ord(plaintext[i]) - (ord(keyword[i]) - 65))) + 1)
        if 97 + (ord(keyword[i]) - 65) <= ord(plaintext[i]) <= 122:
            plaintext[i] = chr(ord(plaintext[i]) - (ord(keyword[i]) - 65))
        elif 97 <= ord(plaintext[i]) <= 97 + (ord(keyword[i]) - 65):
            plaintext[i] = chr(122 - abs(97 - (ord(plaintext[i]) - (ord(keyword[i]) - 65))) + 1)

    plaintext = "".join(plaintext)
    return plaintext