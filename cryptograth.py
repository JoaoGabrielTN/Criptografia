import os, sys
from PIL import Image

# total size = (msg_r+msg_g)*msg_b = TOTAL OF 130050 characters
msg_r = 0
msg_g = 0
msg_b = 0

# crypto rules
msg_cc = 0
msg_jmp = 0
msg_mod = 0

# sign (0 == default)
msg_sig = 0

def read_img:
    filename = "font.png"
    img = Image.open(filename)
    jmp = 0
    ticking = 0
    msg = ""

    width, heigth = img.size

    rgb_img = img.convert('RGB')

    for y in range(heigth):
        for x in range(width):
            jmp+=msg_jmp
            pixel = rgb_img.getpixel((x, y))

            r, g, b = pixel
            if y == 0 and x == 1:
                global msg_r
                msg_r = r # size 1
                global msg_g
                msg_g = g # size 2
                global msg_b
                msg_b = b # mult

            if y == 0 and x == 2:
                global msg_cc
                msg_cc = r
                global msg_jmp
                msg_jmp = g
                global msg_mod
                msg_mod = b

            if y == 0 and x == 3:
                global msg_sig
                msg_sig = r+g+b

            global msg_r
            global msg_g
            global msg_b
            max_size = (msg_r+msg_g)*msg_b
            if ticking <= max_size:
                calc = msg_cc
                msg+=calc(r)+calc(g)+calc(b)

    return msg

def calc:
    # pass parm
    global msg_cc
    global msg_mod
    return chr((num+msg_r+jmp)%msg_mod)
