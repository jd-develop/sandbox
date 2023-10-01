#!/usr/bin/env python3
# coding:utf-8
import qrcode as qrc

qr = qrc.QRCode(
    version=11,
    box_size=3,
    border=5
)

qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("qrcode.png")

from read_qrcode import *
print(val)

# qrc.make("https://blb-studios.github.io").save("qrcode.png")
