#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from PIL import Image


def str2bin(string):
    binary = [bin(ord(c))[2:].zfill(8) for c in string]  # ord(c) converts character to int; bin() converts int to binary with 0b prefix; then slice off 0b with [2:] and pad front with 0's up to 8 bits with zfill(8)
    return binary


def embed(msg, key, inFile):
    binArray = str2bin(msg)  # convert message to binary
    img = Image.open(inFile)  # open the image
    img = img.convert('RGB')  # convert to RGB if not already
    size = img.size  # get dimensions of image
    width = size[0] - 1  # keep in mind arrays start at 0; horizontal size
    height = size[1] - 1  # see previous comment; vertical size

    # determine length of message and store that information first

    arrayLength = len(binArray)  # tells us how many characters in string
    binArray = [bin(arrayLength)[2:].zfill(8)] + binArray #add length of message in binary format to front of our binArray;  max length of message is 255 characters
    
    random.seed(key)  # initializes the internal state of the random number generator
    for byte in binArray:
        for bit in byte:
            x = random.randint(0, width)
            y = random.randint(0, height)
            coordinate = (x, y)
            pixel = img.getpixel(coordinate)  # this returns a 3-tuple
            r = pixel[0]  # we need to save these three items but will only change the LSB of the blue value
            g = pixel[1]
            b = pixel[2]

            # only need to change the LSB when we need to go from 1 to 0 or 0 to 1.  Sometimes we can just leave as is; less things we change more undetectable it is.

            if b % 2 == 0 and bit == '1':  # change
                b = b + 1
                img.putpixel(coordinate, (r, g, b))
            if b % 2 == 1 and bit == '0':  # change
                b = b - 1
                img.putpixel(coordinate, (r, g, b))
    img.save('output.bmp')


if __name__ == '__main__':
    img = raw_input("Please input name of the .bmp image you want to hide your data in: ")
    msg = raw_input("Please input your secret message. The max limit is roughly 255 characters: ")
    num = raw_input("Please input a secret number to initialize the random number generator: ")
    embed(msg, num, img)
    

