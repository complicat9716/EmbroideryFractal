from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# file names
filename = './Images/CU_circle.png'
# filename = './Images/cat.jpg'


##################################################################################
# original image
im = Image.open(filename)
# image information
print('Width: ', im.width)
print('Height: ', im.height)


##################################################################################
# gray scale (light intensity)
im = np.array(Image.open(filename).convert('L'))
# image information
print(im)
print('Shape: ',im.shape)
print(im.flatten())

##################################################################################
# test numpy array
x2 = np.random.randint(10, size = (3, 4))
print('x2 shape: ', x2.shape)
print(x2)


##################################################################################
# gray scale image
plt.gray()
plt.imshow(im)

##################################################################################
plt.figure()
plt.imshow(x2)

##################################################################################
# histogram
plt.figure()
plt.hist(im.flatten(), 255)


plt.show()