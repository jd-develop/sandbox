#!/usr/bin/env python3
# coding:utf-8
import string
import random

accentuated_letters_chunk1_uppercase = "ÀÄÁÂÇÉÈÊËÍÌÎÏÓÒÔÖÚÙÛÜÝỲŶŸ"
accentuated_letters_chunk1_lowercase = accentuated_letters_chunk1_uppercase.lower()

accentuated_letters_chunk2_lowercase = "ĝĉĥĵŝŭ"
accentuated_letters_chunk2_uppercase = accentuated_letters_chunk2_lowercase.upper()

char_list = ["\u0000",
             *string.ascii_uppercase,
             *string.ascii_lowercase,
             *accentuated_letters_chunk1_uppercase,
             *accentuated_letters_chunk1_lowercase,
             *"ŒœÆæ",
             *".…,;’?!",
             *string.digits,
             *"+-×/%‰÷±=≟",
             *"`—_()[]{}©🄯\\",
             " ",  # index 146
             *":«»<>⩽⩾→←↑↓€$#*~",
             *"ñÑ",
             *accentuated_letters_chunk2_lowercase,
             *accentuated_letters_chunk2_uppercase,
             *"®¿¡^²³⁴√∛∜&|↗↖↙↘ẞß⤢⤡≠™¶°·•@",
             *"\n\t",
             *"\"'  ",
             *"£§ħ∀∃⇒⇐⇔Ħ∄¼½¾′″„“”¬¤˙¯ềỀ†‡",
             *"ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
              "αβγδεζηθικλμνξοπρστυφχψω"
              "ϐςϕϵϑϰϖϱϲϒϚϛϘϙϞϟͲͳϠϡϜϝͶͷͰͱϺϻͿϳϷϸȢϗ",
             ]


def cipher(input_text, key):
    if key == "r":
        key = ""
        for i in range(random.randint(10, 15)):
            what_to_do = random.randint(0, 2)
            if what_to_do == 0:
                key += "1"
                key += str(random.randint(1, 9))
            elif what_to_do == 1:
                key += "2"
            elif what_to_do == 2:
                key += "4"
                value = str(random.randint(1, 999))
                while len(value) < 3:
                    value = "0" + value
                key += value
        print(f"Using key {key}")

    output_text = "985"
    for char in input_text:
        if char in char_list:
            coded_char = str(char_list.index(char))
            while len(coded_char) != 3:
                coded_char = "0" + coded_char
            output_text += coded_char
        else:
            unicode = str(ord(char))
            len_unicode = str(len(unicode))
            if len(len_unicode) == 1:
                len_unicode = "0" + len_unicode
            output_text += f"979{len_unicode}{unicode}"

    while key != "":
        print("Computing…")
        if key.startswith("1") and len(key) > 1 and key[1].isdigit():
            shift_value = int(key[1])
            input_shift = output_text
            output_text = f"99{shift_value}"
            for char in input_shift:
                if char.isdigit():
                    output_text += str((int(char)+shift_value) % 10)
                else:
                    output_text += char
            key = key[2:]
        elif key.startswith("2"):
            key = key[1:]
            input_chiffre = output_text
            output_text = "987"
            for char in input_chiffre:
                if char in char_list:
                    coded_char = str(char_list.index(char))
                    while len(coded_char) != 3:
                        coded_char = "0" + coded_char
                    output_text += coded_char
                else:
                    unicode = str(ord(char))
                    len_unicode = str(len(unicode))
                    if len(len_unicode) == 1:
                        len_unicode = "0" + len_unicode
                    output_text += f"979{len_unicode}{unicode}"
        elif key.startswith("4") and len(key) > 3 and key[1:4].isdigit():
            shift_value = int(key[1:4])
            input_shift = output_text
            output_text = f"984{key[1:4]}"
            key = key[4:]
            while len(input_shift) >= 3:
                if input_shift[:3].isdigit():
                    value = str((int(input_shift[:3]) + shift_value) % 1000)
                    while len(value) != 3:
                        value = "0" + value
                    output_text += value
                else:
                    output_text += input_shift[:3]
                input_shift = input_shift[3:]
            output_text += input_shift
        else:
            if key[0] in char_list:
                coded_char = str(char_list.index(key[0]))
                while len(coded_char) != 3:
                    coded_char = "0" + coded_char
                output_text = f"962{coded_char}" + output_text
            else:
                unicode = str(ord(key[0]))
                len_unicode = str(len(unicode))
                if len(len_unicode) == 1:
                    len_unicode = "0" + len_unicode
                output_text = f"961{len_unicode}{unicode}" + output_text

            key = key[1:]

    output_text = "989" + output_text + "988"

    with open("output.txt", "w+", encoding="UTF-8") as of:
        of.write(output_text)
    # print(f"Output: {output_text}")
    return output_text


def decipher(input_text):
    if not input_text.startswith("989") or not input_text.endswith("988"):
        raise Exception("Invalid input")
    input_text = input_text[3:-3]

    output_text = ""
    key_used = ""
    is_ciphered = True
    while is_ciphered:
        print("Computing…")
        if (is_final := input_text.startswith("985")) or input_text.startswith("987"):
            input_text = input_text[3:]
            while input_text != "":
                if input_text[:3] == "979":
                    len_unicode = int(input_text[3:5])
                    input_text = input_text[5:]
                    unicode = ""
                    for i in range(len_unicode):
                        unicode += input_text[0]
                        input_text = input_text[1:]
                    char = chr(int(unicode))
                    output_text += char
                else:
                    index = int(input_text[:3])
                    if index < len(char_list):
                        output_text += char_list[index]
                    else:
                        output_text += char_list[0]
                    input_text = input_text[3:]
            if is_final:
                is_ciphered = False
            else:
                input_text = output_text
                output_text = ""
                key_used = "2" + key_used
        elif input_text.startswith("99"):
            shift_value = int(input_text[2])
            input_text = input_text[3:]
            key_used = f"1{shift_value}" + key_used
            for char in input_text:
                output_text += str((int(char) - shift_value) % 10)
            input_text = output_text
            output_text = ""
        elif input_text.startswith("961"):
            len_unicode = int(input_text[3:5])
            input_text = input_text[5:]
            unicode = ""
            for i in range(len_unicode):
                unicode += input_text[0]
                input_text = input_text[1:]
            char = chr(int(unicode))
            key_used = char + key_used
        elif input_text.startswith("962"):
            input_text = input_text[3:]
            index = int(input_text[:3])
            if index < len(char_list):
                char = char_list[index]
            else:
                char = char_list[0]
            input_text = input_text[3:]

            key_used = char + key_used
        elif input_text.startswith("984"):
            input_text = input_text[3:]
            output_text = ""
            shift_value = int(input_text[0:3])
            key_used = f"4{input_text[0:3]}" + key_used
            input_text = input_text[3:]
            while len(input_text) >= 3:
                if input_text[:3].isdigit():
                    value = str((int(input_text[:3]) - shift_value) % 1000)
                    while len(value) != 3:
                        value = "0" + value
                    output_text += value
                else:
                    output_text += input_text[:3]
                input_text = input_text[3:]
            output_text += input_text

            input_text = output_text
            output_text = ""
        else:
            print(input_text)
            raise Exception("Bad input")

    with open("output.txt", "w+", encoding="UTF-8") as of:
        of.write(output_text)
    with open("key_used.txt", "w+", encoding="UTF-8") as kf:
        kf.write(key_used)

    # print(f"Output: {output_text}")
    # print(f"Key used: {key_used}")
    return output_text, key_used


while (mode := input("Mode (c/d/exit) : ")) != "exit":
    input_mode = input("Input mode (file/line)(f/l) : ")
    if input_mode in ["f", "file"]:
        file_name = input("File path (default: input.txt) : ")
        if file_name == "":
            file_name = "input.txt"
        with open(file_name, "r+", encoding="UTF-8") as f:
            input_text_ = f.read()
    else:
        input_text_ = input("Input: ")

    if mode == "c":
        key_ = input("Key (leave empty for default, r for a random key): ")
        output_ = cipher(input_text_, key_)
    elif mode == "d":
        output_, key_used_ = decipher(input_text_)
