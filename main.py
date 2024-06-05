from vigenere_chiper import *



while True:

    print('======================================================')
    print('Welcome to Vigenere Chiper Program')
    print('Please choose your option below')
    print("=======================================================")
    print('1. Encrypt')
    print("2. Decrypt")
    print("3. Exit")

    option = int(input("Enter your option (number): "))

    if option == 1:
        print('======================================================')
        print('Welcome to Vigenere Chiper Program')
        print('Encrypt your message')
        print("=======================================================")
        plaintext = input("Enter your message that want to encrypt: ")
        key = input("Enter the key to encrypt your message (Your key is classified and wll be used to decrypt your message): ")
        
        print("Here is your encypted message: ")
        print(encrypt(plaintext, key))
        break
    elif option == 2:
        print('======================================================')
        print('Welcome to Vigenere Chiper Program')
        print('Encrypt your message')
        print("=======================================================")
        chipertext = input("Enter your message that want to decrypt: ")
        key = input("Enter the key to decrypt your message (The key that have used to encrypt the message before): ")
        
        print("Here is your decrypted message: ")
        print(decrypt(chipertext, key))
        break
    elif option == 3 :
        break
    else:
        break
