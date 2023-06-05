# coding:utf-8
# Won xumfhërrhghtuwirrh ghtrrhaonwxrrhu lesi phrrhaonwë aon ürrhghtoacrrhigtph gd’igtbigtrrhigt

# Igtlesphigtbesë phümneaghtux wingtblesuphua :
# a
# ã is an
# è
# é
# i
# ĩ is in and un
# e is e ouvert (ə) as in m*on*sieur
# œ is e ouvert (œ) as in fleur or œuf
# ø is e fermé as in vœu
# o is o ouvert as in sort
# ō is o fermé as in bépo
# õ is on
# u is ou
# y is u as in upsilon

# p
# t
# k
# b
# d
# g
# f
# v
# s
# z
# ç is ch as in chat
# j is j as in jardin
# l
# m
# n
# r

input_ipa = input("Enter a French text converted into simplified phonetic alphabet: ")

convert = {
    " ": " ",
    "’": "’",
    "'": "’",
    "a": "igt",
    "ã": "aon",
    "è": "ë",
    "é": "a",
    "i": "u",
    "ĩ": "ingt",
    "e": "on",
    "o": "ü",
    "ō": "oa",
    "õ": "um",
    "u": "e",
    "œ": "i",
    "ø": "e!",
    "y": "eu",

    "p": "b",
    "t": "ght",
    "k": "x",
    "b": "bes",
    "d": "gd",
    "ɡ": "c",
    "g": "c",
    "f": "ph",
    "v": "fh",
    "s": "w",
    "z": "lsh",
    "ç": "zsch",
    "j": "sg",
    "l": "les",
    "m": "hms",
    "n": "mne",
    "ʁ": "rrh",
    "r": "rrh",
}

out = ""
for char in input_ipa:
    out += convert.get(char, "")

print(out)
