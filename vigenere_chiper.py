# This is the Vineger Cipher Program
# This program can Encrypt and Decrypt Words into Vineger Methods
# Created by Azriel Akbar Sofyan


'''
Algorithm
Encryption:

1. Input the word that want to encrypted
2. Input the key for encryption
3. Calculate total letters of word that want to encrypt
4. Create word of sequence based on the key and the total letter of words.
5. Menambahkan antara huruf kata asli dengan huruf dari key yang telah didapatkan.

'''

import numpy as np



# Function to get key of dictionary by its value 
def get_key(val, dictionary):
   
    for key, value in dictionary.items():
        if val == value:
            return key
 
    return "key doesn't exist"

# Encrypt Function
def encrypt(words, key):

    words_values = []
    key_values = []
    chipertext_numbers = []
    chipertext = []
    process = True

    letter_values ={
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }

    # Remove all space in the words
    words = words.replace(' ', '')
    words = words.lower()

    # Remove all space in the key
    key = key.replace(' ', '')
    key = key.lower()

    # Calculate the words lenght that will be encrypted
    total_length_words = int(len(words))

    # Repetite key as same as the total lenght of words
    repetitive_words = key * (total_length_words // len(key) + 1)
    repetitive_words = repetitive_words[:total_length_words]

    for letter in repetitive_words:
        key_values.append(int(letter_values.get(letter)))

    # Iterate throgh word
    # If plaintext is contain number or any symbol, set the the program into False condition
    for letter in words:
        if letter not in letter_values:
            process = False
            break

    if process == True:
        for letter in words:
            words_values.append(int(letter_values.get(letter)))
        
        result_array = np.array(words_values) + np.array(key_values)
        result_list = result_array.tolist()
        
        for i in result_list:
            chipertext_numbers.append(i%26)
        
        for i in chipertext_numbers:
            chipertext.append(get_key(i, letter_values))

        result = ''
        return result.join(chipertext)

    else:
        return 'The plaintext must be a-z, not contain any symbol or nummber'
    # print(result) 
    # print(key_values)
    # print(len(words_values)
    # print(len(key_values))


def decrypt(chipertext, key):

    words_values = []
    key_values = []
    chipertext_numbers = []
    plaintext = []
    process = True

    letter_values ={
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    # Remove all space in the chipertext
    chipertext = chipertext.replace(' ', '')
    # Convert into lowercase
    chipertext = chipertext.lower()

    # Remove all space in the key
    key = key.replace(' ', '')
    key = key.lower()

    # Calculate the words lenght that will be encrypted
    total_length_chipertext = int(len(chipertext))

    # Repetite key as same as the total lenght of words
    repetitive_words = key * (total_length_chipertext // len(key) + 1)
    repetitive_words = repetitive_words[:total_length_chipertext]

    for letter in repetitive_words:
        key_values.append(int(letter_values.get(letter)))

    # Iterate throgh word
    # If plaintext is contain number or any symbol, set the the program into False condition
    for letter in chipertext:
        if letter not in letter_values:
            process = False
            break

    if process == True:
        for letter in chipertext:
            words_values.append(int(letter_values.get(letter)))
        
        result_array = np.array(words_values) - np.array(key_values)
        result_list = result_array.tolist()
        
        for i in result_list:
            chipertext_numbers.append(i%26)
        
        for i in chipertext_numbers:
            plaintext.append(get_key(i, letter_values))

        result = ''
        return result.join(plaintext)

    else:
        return 'The plaintext must be a-z, not contain any symbol or nummber'

