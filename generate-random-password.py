import random

numberList = "1234567890"
upperCaseList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCaseList = upperCaseList.lower()
spcialChars = "!@#$%^&*()_+-=,./<>?;':[]"
allChars = numberList + upperCaseList + lowerCaseList + spcialChars

def insertCharts(keyStr, chars, passwordLength):
    keyList = []
    for i in range(passwordLength):
        keyList.append(keyStr[i])


    rand = random.randint(0, passwordLength - 1)
    keyList[rand] = random.choice(chars)

    key = ''
    for i in range(passwordLength):
        key = key + keyList[i]
    return key

def checkChars(key, chars, passwordLength):
    charsLength = len(chars)
    for i in range(charsLength):
        for j in range(passwordLength):
            if chars[i] == key[j]:
                return False
    return True

def main(passwordLength):

    password = ""
    i = 0
    while i < passwordLength:
        password = password + random.choice(allChars)
        i = i + 1

    while True and passwordLength > 3:
        if checkChars(password, numberList, passwordLength):
            password = insertCharts(password, numberList, passwordLength)
        elif checkChars(password, upperCaseList, passwordLength):
            password = insertCharts(password, upperCaseList, passwordLength)
        elif checkChars(password, lowerCaseList, passwordLength):
            password = insertCharts(password, lowerCaseList, passwordLength)
        elif checkChars(password, spcialChars, passwordLength):
            password = insertCharts(password, spcialChars, passwordLength)
        else:
            break

    return password



passwordLength = int(input("Enter the length of your password => "))

if passwordLength > 0 :
    print("Here is the random password for you => " + main(passwordLength))
else :
    print("Password length has to be at least 1 char long. (thanks for testing though)")
