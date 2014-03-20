#!/usr/bin/python
# This script will implement the prewitt filter
import Image

im = Image.open("LENA512.BMP")

prewitt = Image.new("L", im.size, "black")
sobel = Image.new("L", im.size, "black")

imageW = im.size[0]
imageH = im.size[1]

im.show()

putpixel = im.im.putpixel

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

                # Prewitt calculation
                res = (p1 + p2 + p3 - p7 - p8 - p9) + (p3 + p6 + p9 - p1 - p4 - p7)
                prewitt.putpixel((x, y), res)

                # Sobel calculation
                res = (p1 + (p2 + p2) + p3 - p7 - (p8 + p8) - p9) + (p3 + (p6 + p6) + p9 -p1 - (p4 + p4) - p7)
                sobel.putpixel((x, y), res)


prewitt.show()
sobel.show()

#mod_prewitt = Image.new("L", im.size, "black")

# WeightMatrix = [[0 for x in xrange(3)] for x in xrange(3)] 
# # Initial implementation
# WeightMatrix[1][0] = -4
# WeightMatrix[2][0] = -8
# WeightMatrix[2][1] = -4

# WeightMatrix[0][1] = 4
# WeightMatrix[0][2] = 8
# WeightMatrix[1][2] = 4

# for y in range(0, imageH):
#     for x in range(0, imageW):
#         if y > 0 and y < imageH-1:
#             if x > 0 and x < imageW-1:
#                 for a in range(-1, 1):
#                     for b in range(-1, 1):
#                         mod_prewitt.putpixel((x+b, y+a), mod_prewitt.getpixel((x+b, y+a)) + WeightMatrix[b+1][a+1]*im.getpixel((x, y)))

# mod_prewitt.show()


