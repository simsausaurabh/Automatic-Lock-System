import PIL
from PIL import Image

# taking 1 image and resizing as: 92x112
basewidth = 92
img = Image.open('../training/positive/positive_000.pgm')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(0.525)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('f1.pgm')

# taking 2 image and resizing as: 92x112
img = Image.open('../training/positive/positive_001.pgm')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(0.5)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('f2.pgm')

# taking 3 image and resizing as: 92x112
img = Image.open('../training/positive/positive_002.pgm')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(0.408)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('f3.pgm')

# taking 4 image and resizing as: 92x112
img = Image.open('../training/positive/positive_003.pgm')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(0.395)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('f4.pgm')

# taking 5 image and resizing as: 92x112
img = Image.open('../training/positive/positive_004.pgm')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(0.4)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('f5.pgm')

# taking 6 image and resizing as: 92x112
img = Image.open('../training/positive/positive_005.pgm')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(0.365)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('f6.pgm')