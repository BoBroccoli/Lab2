import sys
from random import *
from PIL import Image
#imageName = raw_input("Please enter the image you want to use: ")
param_1 = sys.argv[1]
if(param_1 == 'encode'):
    picName = randint(1,5)
    print('Radom selected: ' + str(picName) + '.png')
    im = Image.open( str(picName) + '.png')
    sentense = raw_input("Please enter the sentense you want to encode: ")
    binaryList = []
    for char in sentense:
        binaryList.append( '00000000'[len(bin(ord(char))[2:]):] + bin(ord(char))[2:] )
    binaryList.append('11111110')
    #binaryList.append('10000000')
    #print binaryList
    #Just a comment
    width, height = im.size
    #1024 1024
    rgb_im = im.convert('RGB')
    i = 0
    ################
    (r,g,b) = rgb_im.getpixel((width - 1, height - 1));
    loc = g
    ################
    while (i < len(binaryList) * 8):
        r, g, b = rgb_im.getpixel(( i % width, i / width))
        #for each b change last bit to binaryList
        binaryB = bin(int(hex(b)[2:], 16))[2:].zfill(8)
        #print binaryB
        binaryB = binaryB[:-1] + binaryList[i / 8][i % 8]
        #print binaryB
        binaryB = int(str(binaryB), 2)
        b = binaryB
        rgb_im.putpixel((loc % width, loc / width), (r,g,b))
        ##################
	loc = loc + (r % 16) + 1
        ##################
        i = i + 1
     rgb_im.save('secret.png')
    
    print 'encoded'
else:
    im = Image.open('secret.png');
    width, height = im.size;
    imsize = width * height;

    rgb_im = im.convert('RGB');
    
    (r,g,b) = rgb_im.getpixel((width - 1, height - 1));
    loc = g;
    msg_bits = [];
    (r,g,b) = rgb_im.getpixel((loc % width, loc / width));
	
    # iterate until reach a (0,0,0) pixel
    # collect the bit string in msg_bits
    pad = 0
    
    while( (loc < imsize - 1) & (pad != 2 ** 8 - 2) ):
        if((b % 2) == 0):
            msg_bits.append('0');
	    pad = (pad * 2) % (2 ** 8);
        else:
            msg_bits.append('1');
	    pad = (pad * 2 + 1) % (2 ** 8);
        loc = loc + (r % 16) + 1;
        (r,g,b) = rgb_im.getpixel((loc % width, loc / width));
		
    bstr = "".join(msg_bits);

    # reconstruct msg
    i = 0;
    msg = [];
    # get rid of the padding
    bstr = bstr[0:-8]
    while( i < len(bstr) ):
        letter = chr(int(bstr[i:i+8],2));
        msg.append(letter);
        i = i + 8;
    pt = "".join(msg);

    print "the plain text is: "  + pt;
    print 'decoded';

