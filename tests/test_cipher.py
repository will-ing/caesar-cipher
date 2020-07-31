from caesar_cipher.cipher import encrypt, decrypt, break_caesar
import sys
import io


def test_encrypt():
    assert encrypt('hello world', 2) == 'jgnnq yqtnf'


def test_decrypt():
    assert decrypt('jgnnq yqtnf', 2) == 'hello world'


def test_break():
    assert break_caesar('hkpf jgnr') == 'find help '


def test_upper():
    assert break_caesar('hKpF jGnr') == 'find help '


def test_upper():
    message = encrypt('It was the best of times, it was the worst of times', 2)
    assert break_caesar(
        message) == 'It was the best of times, it was the worst of times '
