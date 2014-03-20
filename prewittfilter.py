#!/usr/bin/python
# This script will implement the prewitt filter
import Image

im = Image.open("LENA512.BMP")

im.show()

orig_prewitt = Image.new("L", im.size, "black")

imageW = im.size[0]
imageH = im.size[1]

putpixel = im.im.putpixel

# for y in range(0, imageH):
#     for x in range(0, imageW):
#         if y > 0 and y < imageH-1:
#             if x > 0 and x < imageW-1:
#                 p1 = im.getpixel((x-1, y-1))
#                 p2 = im.getpixel((x, y-1))
#                 p3 = im.getpixel((x+1, y-1))
#                 p4 = im.getpixel((x-1, y))

#                 p6 = im.getpixel((x+1, y))
#                 p7 = im.getpixel((x-1, y+1))
#                 p8 = im.getpixel((x, y+1))
#                 p9 = im.getpixel((x+1, y+1))

#                 res = (p1 + p2 + p3 - p7 - p8 - p9) + (p3 + p6 + p9 - p1 - p4 - p7)
                       
#                 orig_prewitt.putpixel((x, y), res)
# orig_prewitt.show()

mod_prewitt = Image.new("L", im.size, "black")

WeightMatrix = [[0 for x in xrange(3)] for x in xrange(3)] 
# Initial implementation
WeightMatrix[1][0] = -1
WeightMatrix[2][0] = -2
WeightMatrix[2][1] = -1

WeightMatrix[0][1] = 1
WeightMatrix[0][2] = 2
WeightMatrix[1][2] = 1

for y in range(0, imageH):
    for x in range(0, imageW):
        if y > 0 and y < imageH-1:
            if x > 0 and x < imageW-1:
                for a in range(-1, 1):
                    for b in range(-1, 1):
                        mod_prewitt.putpixel((x+b, y+a), mod_prewitt.getpixel((x+b, y+a)) + WeightMatrix[b+1][a+1]*im.getpixel((x, y)))

                # mod_prewitt.putpixel((x,   y-1), mod_prewitt.getpixel((x,   y-1)) + WeightMatrix[x     % 3][(y-1) % 3]*im.getpixel((x, y)))
                # mod_prewitt.putpixel((x+1, y-1), mod_prewitt.getpixel((x+1, y-1)) + WeightMatrix[(x+1) % 3][(y-1) % 3]*im.getpixel((x, y)))
                # mod_prewitt.putpixel((x+1, y  ), mod_prewitt.getpixel((x+1, y  )) + WeightMatrix[(x+1) % 3][y     % 3]*im.getpixel((x, y)))

                # mod_prewitt.putpixel((x-1, y  ), mod_prewitt.getpixel((x-1, y  )) + WeightMatrix[(x-1) % 3][y     % 3]*im.getpixel((x, y)))
                # mod_prewitt.putpixel((x-1, y+1), mod_prewitt.getpixel((x-1, y+1)) + WeightMatrix[(x-1) % 3][(y+1) % 3]*im.getpixel((x, y)))
                # mod_prewitt.putpixel((x,   y+1), mod_prewitt.getpixel((x,   y+1)) + WeightMatrix[x     % 3][(y+1) % 3]*im.getpixel((x, y)))

mod_prewitt.show()


