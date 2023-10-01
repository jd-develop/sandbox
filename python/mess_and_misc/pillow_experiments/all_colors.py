#!/usr/bin/env python3
# coding:utf-8
from PIL import Image

image = Image.new("RGB", (4096, 4096))

x, y = 0, 0
for r in range(256):
    for g in range(256):
        for b in range(256):
            image.putpixel((x, y), (r, g, b))
            x += 1
            if x == 4096:
                x = 0
                y += 1

image.save("./all_colors.png", "PNG")
