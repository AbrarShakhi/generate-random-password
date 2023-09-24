def length(minimum=4):
    isValidInput = False

    while not isValidInput:
        isValidInput = True
        try:
            passwordLength = int(input("Length of the password (password > 3): "))
            if passwordLength == 0:
                exit()
            if passwordLength < minimum:
                print("Password length should be greater than 3. Or enter 0 to exit.")
                isValidInput = False
        except Exception as e:
            print("Please enter a valid number. Or enter 0 to exit.")
            isValidInput = False

    return passwordLength