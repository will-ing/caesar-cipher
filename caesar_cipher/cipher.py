# pylint: disable=unused-variable
import string
from nltk.corpus import words
import nltk


def encrypt(entry, key):
    """
    Method that uses the caesar cipher to encrypt strings.

    Step checkers
    print(f'ALPH: {alph_lower}')
    print(f'shift: {shift_it}')
    print(f'tb: {tb}')

    REF: https://www.tutorialspoint.com/python3/string_maketrans.htm \n
    #:~:text=Itertools.Product()-,Python%20string%20%7C%20ascii_lowercase,the%20lowercase%20letters%20 \n
    REF: https://www.geeksforgeeks.org/python-string-ascii_lowercase/
    REF: https://www.programiz.com/python-programming/methods/string/translate

    Args:
        entry (str): Any String
        key (int): Any integer

    Returns:
        str: Encrypted string
    """

    alph_lower = string.ascii_lowercase
    shift_it = alph_lower[key:] + alph_lower[:key]
    tb = str.maketrans(alph_lower, shift_it)
    return entry.translate(tb)


def decrypt(entry, key):
    return encrypt(entry, -key)


def binarySearch(arr, x):
    """
    searches for the index of the arr and value that are passed through.
    If the value does not exist it will return -1
    arg(arr) = an array of any length
    arg(x) = x is the value you want to search
    """

    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid]
        elif x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            break
    return False


def break_caesar(encrypted):
    """
    Hacks a caesar cipher using dict of words. Some of the words don't exist in the dict. You can print the list of possible words by adding: print(splitting)

    Args:
        encrypted (str): an encrypted caesar cipher

    Returns:
        [str]: A string of the most likely outcome
    """

    chars = string.ascii_lowercase
    shifting = str.maketrans(chars, chars[1:]+chars[:1])

    mess = encrypted.lower()
    word_dict = words.words()

    answer = ''

    for i in range(0, 25):
        splitting = mess.split()

        for i in splitting:
            result = binarySearch(word_dict, i)
            if result and result != None:
                answer += f'{result} '

        mess = mess.translate(shifting)

    return answer
