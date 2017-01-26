def encrypt(text, rot):

    encryptedText = ""
    while len(text) != 0:
        for char in text:
            encryptedText = encryptedText + rotate_character(char, rot)
        break
    return encryptedText


def alphabet_position(letter):
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.isalpha():
        if letter.islower():
            i = alpha_lower.find(letter)
        elif letter.isupper():
            i = alpha_upper.find(letter)
    else:
        i = letter

    return i


def rotate_character(char, rot):
    charPos = alphabet_position(char)

    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted =  ""

    if char.isalpha():

        rotatedIndex = charPos + rot

        if char.isupper():
            if rotatedIndex < 26:
                encrypted = encrypted + alpha_upper[rotatedIndex]
            else:
                encrypted = encrypted + alpha_upper[rotatedIndex % 26]
        elif char.islower():
            if rotatedIndex < 26:
                encrypted = encrypted + alpha_lower[rotatedIndex]
            else:
                encrypted = encrypted + alpha_lower[rotatedIndex % 26]

    else:
        rotatedIndex = charPos
        encrypted = encrypted + rotatedIndex

    return encrypted
