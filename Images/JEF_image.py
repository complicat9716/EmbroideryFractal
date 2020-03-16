import numpy
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from JEF_class import JEF


# The function takes image file path as input, save the image to the specified location and binarilize the image at a specific threshold
def binary_image(img_path, targetPath, threshold):
    # load image
    image_file = Image.open(img_path)

    # convert image to light intensity
    image = image_file.convert('L')
    image = numpy.array(image)

    # binarlize image
    image = binarize_array(image, threshold)

    # show gray scale image
    plt.gray()
    plt.imshow(image)

    print(image.shape)

    plt.show()


# loop through the image array
def binarize_array(numpy_array, threshold = 200):
    # for each row
    for i in range(len(numpy_array)):

        # if it is a even row
        if i%2 == 0:

            # read the image from left to right
            for j in range(len(numpy_array[0])):

                # if there is a black pixel make a stitch, else move the same distance
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                    Embroideryfile.moveRight()
                else:
                    numpy_array[i][j] = 0
                    Embroideryfile.sewRight()

        # if it is a odd row
        else:

            # read the image from right to left
            for j in reversed(range(len(numpy_array[0]))):

                # if there is a black pixel make a stitch, else move the same distance
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                    Embroideryfile.moveLeft()
                else:
                    numpy_array[i][j] = 0
                    Embroideryfile.sewLeft()

        # move the thread down after each row
        Embroideryfile.moveDown()

    return numpy_array


if __name__ == "__main__":

    Embroideryfile = JEF("Image_JEF_test.jef", 3, [1, 5, 6])

    filename = './Images/Black_Crown.jpg'
    targetPath = './Images/Crown_Binary.jpg'
    binary_image(filename, targetPath, 125)

    # File generation
    Embroideryfile.generatefile()


    