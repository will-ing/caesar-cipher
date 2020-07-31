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
    ent = entry.lower()
    remove_char = ent.translate(str.maketrans('', '', "!?,.'"))
    return remove_char.translate(tb)


def decrypt(entry, key):
    return encrypt(entry, -key)


def binarySearch(arr, x):
    """
    Searches an array for a value.

    Big O: O(log n)

    Args:
        arr ([list]): [any ordered list]
        x ([string or int]): [any value in the list]

    Returns:
        [string]: [value that you wanted out of the array]
    """

    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) / 2
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
    checker = list()
    answer = ' '

    for i in range(0, 26):
        splitting = mess.split()
        # print(splitting)

        # print(f'Checker: {len(checker)}')
        # print(f'splitting: {len(splitting)}')

        if len(checker) == len(splitting):
            answer = answer.join(checker)

        else:
            checker = []
            for i in splitting:
                if i in word_dict:
                    print(f'I : {i}')

                    checker.append(i)
            mess = mess.translate(shifting)
    print(answer)
    return answer


break_caesar(encrypt('It was the best of times, it was the worst of times', 2))
