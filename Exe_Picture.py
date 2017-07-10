#!/usr/bin/python
from PIL import Image

im = Image.open("photo.png")
# photo_new.png <- photo.png
im.save('photo_new.png', 'png')

#create thumbnail
im.thumbnail((100, 100))

im.save('photo_thumbnail.png', 'png')

# http://pillow.readthedocs.org/en/latest/index.html
