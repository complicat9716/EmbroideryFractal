from JEF_class import JEF
import numpy
from PIL import Image
import matplotlib.pyplot as plt

# set up the embroidery file
jefName = "Image_test.jef"
Embroideryfile = JEF(jefName)

# read image into embroidery file as binary image
filename = './Images/CU.png'
Embroideryfile.readImage(filename, 160)

# show original image
image_file = Image.open(filename)
plt.imshow(image_file)
plt.show()

##############################################################################################
# File generation
Embroideryfile.generatefile()

