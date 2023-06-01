#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pprint
# import unicodedata
# import string
import os
import pathlib
import sys


def format_correctly(str_: str):
    return str(str_).replace(" ", "\n").splitlines()


def do_the_math(sentence_: list[str]):
    print("Analyzing...")
    groups_of_letters_ = {}
    existing_groups = []
    for i, word in enumerate(sentence_):
        print(f"word {i+1}/{len(sentence)} ({100 * (i+1)/len(sentence)} %)")
        for pos, letter in enumerate(word):
            if pos + 1 == len(word):
                if letter.lower() in existing_groups:
                    groups_of_letters_[letter.lower()] += 1
                else:
                    groups_of_letters_[letter.lower()] = 1
                    existing_groups.append(letter.lower())
            elif pos + 2 == len(word):
                if letter.lower() + word[pos + 1].lower() in existing_groups:
                    groups_of_letters_[letter.lower() + word[pos + 1].lower()] += 1
                else:
                    groups_of_letters_[letter.lower() + word[pos + 1].lower()] = 1
                    existing_groups.append(letter.lower() + word[pos + 1].lower())
            elif pos + 3 == len(word):
                if letter.lower() + word[pos + 1:pos + 3].lower() in existing_groups:
                    groups_of_letters_[letter.lower() + word[pos + 1:pos + 3].lower()] += 1
                else:
                    groups_of_letters_[letter.lower() + word[pos + 1:pos + 3].lower()] = 1
                    existing_groups.append(letter.lower() + word[pos + 1:pos + 3].lower())
            else:
                group = letter.lower() + word[pos + 1:pos + 4].lower()
                if group in existing_groups:
                    groups_of_letters_[group] += 1
                else:
                    groups_of_letters_[group] = 1
                    existing_groups.append(group)
    print("finish")
    return groups_of_letters_


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
    groups = do_the_math(sentence)
elif mode == "f":
    path_to_file = os.path.abspath(f'{pathlib.Path(__file__).parent.absolute()}/file.txt')
    confirmation = str(input(f"Is the file stored in {path_to_file}? (Y/N): "))
    if confirmation.lower() == "y":
        if os.path.exists(path_to_file):
            with open(path_to_file, encoding='UTF-8') as file:
                sentence = format_correctly(file.read())
                file.close()
            groups = do_the_math(sentence)
        else:
            print("The file doesn't exist...")
            sys.exit()
    else:
        print("OK. Please put the file in the path below and try again! :)")
        sys.exit()

print("formatting...")
value = pprint.pformat(groups)
path_ = os.path.abspath(f'{pathlib.Path(__file__).parent.absolute()}/output.txt')
print(f"dumping into {path_}...")
with open(path_, 'w+', encoding="UTF-8") as f:
    f.write(value)
print(f"The dictionnary is in {path_}")
