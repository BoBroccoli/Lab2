from PIL import Image
import sys
param_1 = sys.argv[1]
param_2 = sys.argv[2]
im1 = Image.open(param_1)
rgb_im1 = im1.convert('RGB')
im2 = Image.open(param_2)
rgb_im2 = im2.convert('RGB')
i = 0
width, height = im1.size
#print width, height
for w in range(width):
    #print i%width, i/height
    for h in range(height):
        r1,g1,b1 = rgb_im1.getpixel(( w, h))
        r2,g2,b2 = rgb_im2.getpixel(( w, h))
        if(b1 != b2):
            rgb_im1.putpixel((w, h),(0,0,0))
        else:
            rgb_im1.putpixel((w, h),(255,255,255))
rgb_im1.save('AnalysisPic.png')
