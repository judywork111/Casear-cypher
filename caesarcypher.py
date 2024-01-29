import time  # import time module
# ---------------------------- define functions-----------------------------
def get_key():
    while True:
        key = input("give a key (for example,3):")
        if key.isdigit():  # check if all characters in a string are digits (0-9)
            shift = int(key)  # Convert the input to an integer
            break
        else:
            print("Wrong input: give an integer again.")
    return shift
# define function : encrypt with a given key k
def encrypt(to_encrypt, shift):
    # reference alphabet
    LowerCaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    HigherCaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""
    # for loop to encrypt letter one by one, encrypt rule = right shift
    for LetterToEncrypt in to_encrypt:
        # encrypt lower case letter
        if LetterToEncrypt in LowerCaseAlphabet:
            AlphabetPosition = LowerCaseAlphabet.index(LetterToEncrypt)  # find letter's position in Lower Case Alphabet
            # use the modulo operator % to ensure that the index stays within len(alphabet)=26
            PositionIndex = (AlphabetPosition + shift) % 26  # use given key to right shift and find new position
            EncryptedLetter = LowerCaseAlphabet[PositionIndex]
        # encrypt higher case letter
        elif LetterToEncrypt in HigherCaseAlphabet:
            AlphabetPosition = HigherCaseAlphabet.index(LetterToEncrypt)
            PositionIndex = (AlphabetPosition + shift) % 26
            EncryptedLetter = HigherCaseAlphabet[PositionIndex]
        # symbol without encrypting
        else:
            EncryptedLetter = LetterToEncrypt
        # append each encrypted letter or symbol in string
        encrypted = encrypted + EncryptedLetter
    return encrypted  # return encrypted sentence
# define function : decrypt with a given key k
def decrypt(to_decrypt, shift):
    LowerCaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    HigherCaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted = ""
    # for loop to decrypt letter one by one, decrypt rule = left shift
    for LetterToDecrypt in to_decrypt:
        # decrypt lower case letter
        if LetterToDecrypt in LowerCaseAlphabet:
            AlphabetPosition = LowerCaseAlphabet.index(LetterToDecrypt)  # find letter's position in Lower Case Alphabet
            # use the modulo operator % to ensure that the index stays within len(alphabet)=26
            PositionIndex = (AlphabetPosition - shift) % 26  # use given key to left shift and find new position
            DecryptedLetter = LowerCaseAlphabet[PositionIndex]
        # decrypt higher case letter
        elif LetterToDecrypt in HigherCaseAlphabet:
            AlphabetPosition = HigherCaseAlphabet.index(LetterToDecrypt)
            PositionIndex = (AlphabetPosition - shift) % 26
            DecryptedLetter = HigherCaseAlphabet[PositionIndex]
        # symbol without decrypting
        else:
            DecryptedLetter = LetterToDecrypt
        # append each decrypted letter or symbol in string
        decrypted = decrypted + DecryptedLetter
    return decrypted  # return encrypted sentence
# define function : find the key k
def hack_key(ciphertext):
    LowerCaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    HigherCaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # loop through every possible key
    for key in range(26):
        plaintext = ""
        # Loop through each position in ciphertext
        for LetterToDecrypt in ciphertext:
            # decrypt lower case letter
            if LetterToDecrypt in LowerCaseAlphabet:
                AlphabetPosition = LowerCaseAlphabet.index(LetterToDecrypt)  # find letter's position in Lower Case Alphabet
                PositionIndex = AlphabetPosition - key  # use given key to left shift and find new position
                # in case after subtracting key, index becomes negative
                if PositionIndex < 0:
                    PositionIndex = PositionIndex + 26  # len(Alphabet)=26
                DecryptedLetter = LowerCaseAlphabet[PositionIndex]
            # decrypt higher case letter
            elif LetterToDecrypt in HigherCaseAlphabet:
                AlphabetPosition = HigherCaseAlphabet.index(LetterToDecrypt)
                PositionIndex = AlphabetPosition - key
                if PositionIndex < 0:
                    PositionIndex = PositionIndex + 26
                DecryptedLetter = HigherCaseAlphabet[PositionIndex]
            # symbol without decrypting
            else:
                DecryptedLetter = LetterToDecrypt
            # append each decrypted letter or symbol in plaintext
            plaintext = plaintext + DecryptedLetter
        # show all possible plaintext of each key
        print("key #%s:%s" %(key,plaintext))

# -------------------------------------user interface------------------------------------------------------
time_start = time.time()  # time.time():Returns the current time in seconds
print("Ready to use Caesar ciphers toolbox...")
while True:  # Create an infinite loop
    user_input = input("Choose your tool number: 1.encrypt 2.decrypt 3.hack key 4.exit 5.auto-substitution \n")
    # choose 4.exit
    if user_input == "4":
        break # exit the loop
    # choose 1.encrypt
    elif user_input == "1":
        to_encrypt = input("Type the sentence you want to encrypt: ")  # get sentence to encrypt
        shift = get_key()  # get a valid key
        encrypted = encrypt(to_encrypt, shift)  # call encrypt function
        print("The encrypted sentence is: " + encrypted)
    # choose 2.decrypt
    elif user_input == "2":
        to_decrypt = input("Type the sentence you want to decrypt: ") # get sentence to decrypt
        shift = get_key()  # get a valid key
        decrypted = decrypt(to_decrypt, shift)  # call decrypt function
        print("The decrypted sentence is: " + decrypted)
    # choose 3.hack key
    elif user_input == "3":
        ciphertext = input("Type the ciphertext you get:")
        print("look through all decryption results for each possible key:")
        hack_key(ciphertext)  # call hack_key function
    # choose 5.auto-substitution
    elif user_input == "5":
        # auto-encrypt
        to_encrypt = input("Type the sentence you want to encrypt: ")  # get sentence to encrypt
        shift = len(to_encrypt)  # key is the length of sentence
        encrypted = encrypt(to_encrypt, shift)  # call encrypt function
        print("The key is: " + str(shift))  # find key
        print("The encrypted sentence is: " + encrypted)
        # auto-decrypt
        to_decrypt = input("Type the sentence you want to decrypt: ")  # get sentence to decrypt
        shift = len(to_decrypt)  # key is the length of sentence
        decrypted = decrypt(to_decrypt, shift)  # call decrypt function
        print("The key is: " + str(shift))  # find key
        print("The decrypted sentence is: " + decrypted)
    # in case wrong choice
    else:
        print("Wrong input: please type 1,2,3,4 or 5 again.")  # remind the user of input errors
    print("\n(Automatically return to menu, if want to exit, choose 4)")
time_exit = time.time()  # Returns the exit time in seconds
time = time_exit - time_start  # calculate total time
print("\nExit Caesar ciphers toolbox...Total time ", time, " seconds\nThank you for using.")