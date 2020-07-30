from caesar_cipher.cipher import encrypt, decrypt, break_caesar
import sys
import io


def test_encrypt():
    assert encrypt('hello world', 2) == 'jgnnq yqtnf'


def test_decrypt():
    assert decrypt('jgnnq yqtnf', 2) == 'hello world'


def test_break():
    assert break_caesar('hkpf jgnr') == 'find help '
