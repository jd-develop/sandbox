#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from unidecode import unidecode
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere(str_:str , key: str, deciphr = False):
    """Chiffre (ou déchiffre si deciphr est à True) par Vigenère la chaîne str_ avec la clef key"""
    if len(str_) == 0:
        return 0
    if len(key) == 0:
        return str_
    key_i = 0
    str_ = unidecode(str_)
    key = unidecode(key).upper()
    final_str = ""
    for char in str_:
        is_upper = char.isupper()
        char = char.upper()
        if char not in ALPHABET or key[key_i] not in ALPHABET:
            final_str += char
            continue

        key_i_in_alphabet = ALPHABET.index(key[key_i])
        char_i_in_alphabet = ALPHABET.index(char)

        if deciphr:
            final_char_i = char_i_in_alphabet - key_i_in_alphabet
        else:
            final_char_i = char_i_in_alphabet + key_i_in_alphabet
        final_char_i %= 26

        if not is_upper:
            final_str += ALPHABET[final_char_i].lower()
        else:
            final_str += ALPHABET[final_char_i]

        key_i += 1
        key_i %= len(key)
    return final_str

