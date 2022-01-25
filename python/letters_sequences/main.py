#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pprint
import unicodedata
import string
import os


def format_correctly(str_: str):
    str_ = str_.lower()
    str_ = unicodedata.normalize('NFD', str_).encode('ascii', 'ignore').decode("utf-8")  # delete accents
    str_ = str_.translate(str.maketrans('', '', string.punctuation))  # delete ponctuation
    return str(str_).replace(" ", "\n").splitlines()


def make_couple_of_letters_from_sentence(sentence_: list[str]):
    couples_of_letters_ = {}
    existing_couples = []
    for word in sentence_:
        for pos, letter in enumerate(word):
            if pos + 1 == len(word):
                if letter in existing_couples:
                    couples_of_letters_[letter] += 1
                else:
                    couples_of_letters_[letter] = 1
                    existing_couples.append(letter)
            else:
                couple = letter + word[pos + 1]
                if couple in existing_couples:
                    couples_of_letters_[couple] += 1
                else:
                    couples_of_letters_[couple] = 1
                    existing_couples.append(couple)
    return couples_of_letters_


is_mode_given = False
mode = None
while not is_mode_given:
    mode = str(input("Enter mode (f: file, i: input): "))
    if mode == "f" or mode == "i":
        is_mode_given = True
    else:
        print("Please write f or i.")

if mode == "i":
    sentence = format_correctly(str(input("Please write a sentence: ")))
    couples_of_letters = make_couple_of_letters_from_sentence(sentence)
    pprint.pprint(couples_of_letters)
elif mode == "f":
    path_to_file = os.path.abspath('./file.txt')
    confirmation = str(input(f"Is the file stored in {path_to_file}? (Y/N): "))
    if confirmation.lower() == "y":
        if os.path.exists(path_to_file):
            with open(path_to_file, encoding='UTF-8') as file:
                sentence = format_correctly(file.read())
                file.close()
            couples_of_letters = make_couple_of_letters_from_sentence(sentence)
            pprint.pprint(couples_of_letters)
        else:
            print("The file doesn't exist...")
    else:
        print("OK. Please put the file in the path below and try again! :)")
