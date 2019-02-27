#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from PIL import Image

def extract(key, inFile):
    random.seed(key)  # initiate random number generator; this gives us same order
    img = Image.open(inFile)
    size = img.size
    width = size[0] - 1
    height = size[1] - 1

    # determine length of message

    count = 0
    length = ''
    while count < 8:  # length is limited to 255 characters because 2^8 = 256
        x = random.randint(0, width)
        y = random.randint(0, height)
        count = count + 1
        coordinate = (x, y)
        pixel = img.getpixel(coordinate)
        if pixel[2] % 2 == 0:
            length = length + '0'
        else:
            length = length + '1'
            
    length = int(length, 2)  # the 2 is because we are using base 2 (aka) as input
    
 
    # use length to know how many bits to retrieve

    count2 = 0
    binArray = []
    byte = ''
    while count2 < length * 8: #because length is in bytes not bits we need to multiply by 8 to know how many bits to recovery since we only store one bit per pixel (inefficient but harder to detect)
        x = random.randint(0, width)
        y = random.randint(0, height)
        coordinate = (x, y)
        pixel = img.getpixel(coordinate)
        if pixel[2] % 2 == 0:
            byte = byte + '0'
        else:
            byte = byte + '1'
        if len(byte) == 8:  # do we have a whole byte yet?
            binArray.append(byte)
            byte = ''  # byte is empty again
        count2 = count2 + 1 #increment to keep track of current length

    # convert list of binary bytes back to integers and then characters

    secretMessage = ''
    for x in binArray:
        num = int(x, 2) #cast binary number to integer
        secretMessage = secretMessage + chr(num) #cast integer to ascii character
    print secretMessage
    
if __name__ == '__main__':
    img = raw_input("Please input name of the .bmp image you want extract the message from: ")
    num = raw_input("Please input the secret key: ")
    extract(num, img)
