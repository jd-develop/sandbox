#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pickle

dict1 = {
    "a": 1,
    "b": [1, 2, 3],
    "c": "abc",
    "d": ("str", 1)
}

file = open('file.bin', 'wb+')
pickle.dump(dict1, file, pickle.HIGHEST_PROTOCOL)
pickle.dump(["str", 4, 6, (23, 12)], file, pickle.HIGHEST_PROTOCOL)
pickle.dump(pickle, pickle.HIGHEST_PROTOCOL)
file.close()


file2 = open('file.bin', 'rb+')
print(pickle.load(file2))
print(pickle.load(file2))
print(pickle.load(file2))
file2.close()
