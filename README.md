This is a simple python tool that will take in a bitmap image and a secret key from the user and use it to randomly generate a pseudorandom sequence of numbers in order to choose which pixels in the image to edit in order to store a short message (less than 255 pixels) by editing the least significant bit in the pixels. The extract tool will then take in an image that has a hidden secret message and recover the message assuming the user enters in the correct secret key
