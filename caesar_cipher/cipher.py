import string


def encrypt(entry, key):
    """
    Method that uses the caesar cipher to encrypt strings. 

    Step checkers
    print(f'ALPH: {alph_lower}')
    print(f'shift: {shift_it}')
    print(f'tb: {tb}')

    REF: https://www.tutorialspoint.com/python3/string_maketrans.htm \n
    REF: https://www.geeksforgeeks.org/python-string-ascii_lowercase/#:~:text=Itertools.Product()-,Python%20string%20%7C%20ascii_lowercase,the%20lowercase%20letters%20 \n
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


print(encrypt('hello world', 2))


def decrypt(entry, key):
    return encrypt(entry, -key)


print(decrypt('jgnnq yqtnf', 2))


def break_caesar(encrypted):
    pass
