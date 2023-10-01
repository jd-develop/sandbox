#!/usr/bin/env python3
# coding:utf-8
import cv2

qrcDetector = cv2.QRCodeDetector()

val, points, qrc = qrcDetector.detectAndDecode(cv2.imread("qrcode.png"))
