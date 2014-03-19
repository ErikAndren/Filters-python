#!/usr/bin/python
# This script will implement the prewitt filter
import Image

im = Image.open("LENA512.BMP")

im.show()

orig_prewitt = Image.new("L", im.size, "black")

imageW = im.size[0]
imageH = im.size[1]

for y in range(0, imageH):
    for x in range(0, imageW):
        if y > 0 and y < imageH-1:
            if x > 0 and x < imageW-1:
                p1 = im.getpixel((x-1, y-1))
                p2 = im.getpixel((x, y-1))
                p3 = im.getpixel((x+1, y-1))
                p4 = im.getpixel((x-1, y))

                p6 = im.getpixel((x+1, y))
                p7 = im.getpixel((x-1, y+1))
                p8 = im.getpixel((x, y+1))
                p9 = im.getpixel((x+1, y+1))

                res = (p1 + p2 + p3 - p7 - p8 - p9) + (p3 + p6 + p9 - p1 - p4 - p7)
                       
                orig_prewitt.putpixel((x, y), res)
orig_prewitt.show()

mod_prewitt = Image.new("L", im.size, "black")

for y in range(0, imageH):
    for x in range(0, imageW):
        if y > 0 and y < imageH-1:
            if x > 0 and x < imageW-1:
                p1 = im.getpixel((x-1, y-1))
                p2 = im.getpixel((x, y-1))
                p3 = im.getpixel((x+1, y-1))
                p4 = im.getpixel((x-1, y))

                p6 = im.getpixel((x+1, y))
                p7 = im.getpixel((x-1, y+1))
                p8 = im.getpixel((x, y+1))
                p9 = im.getpixel((x+1, y+1))

                res = p2 + (2*p3) - p4 + p6 - (2*p7) - p8
                       
                mod_prewitt.putpixel((x, y), res)

mod_prewitt.show()


