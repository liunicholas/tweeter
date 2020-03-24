import random
import string

def encode(pw):
    #list of strings to make random
    strNumList = ["0","1","2","3","4","4","5","6","7","8","9"]
    randCharList = list(string.ascii_lowercase) + list(string.ascii_uppercase) + strNumList
    #amount of fake letters changes every time
    encodeLength = random.randrange(50,70)
    #letter changes evry time
    encodeChar = random.choice(randCharList)
    encodedpw = ""
    for i in range(len(pw)):
        fakeLetterCount = 0
        #different spot for encodedChar each time
        encodeCharSpot = random.randrange(1, encodeLength - 1)

        while fakeLetterCount < encodeLength:
            if fakeLetterCount == encodeCharSpot and encodeChar != pw[i]:
                encodedpw += encodeChar

            else:
                fakeLetter = random.choice(randCharList)
                while fakeLetter == encodeChar:
                    fakeLetter = random.choice(randCharList)
                encodedpw += fakeLetter
            fakeLetterCount += 1

        encodedpw += pw[i]

    return encodedpw, encodeChar

def decode(encodedpw, secretChar):

    charsInpw = 0
    decodedpw = ""

    for char in encodedpw:
        if char == secretChar:
            charsInpw += 1

    if charsInpw == 0:
        return "NA"

    fakeLetters = len(encodedpw) / charsInpw

    for i in range(1, charsInpw + 1):
        decodedpw += encodedpw[int(fakeLetters * i - 1)]

    return decodedpw

# def main():
#     a,b = encode("ethaniscute")
#     print(a)
#
# main()
