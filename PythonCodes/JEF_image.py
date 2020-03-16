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
    plt.imshow(image[0:300, 0:150])

    print(image.shape)

    # show histogram
    plt.figure()
    plt.hist(image.flatten())

    plt.show()

    # save image
    #cv2.imwrite(targetPath, image)

# loop through the image array
def binarize_array(numpy_array, threshold = 200):
    # for each row
    for i in range(len(numpy_array)):

        if i%2 == 0:
            for j in range(len(numpy_array[0])):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                    Embroideryfile.moveRight()
                else:
                    numpy_array[i][j] = 0
                    Embroideryfile.sewRight()
        else:
            for j in reversed(range(len(numpy_array[0]))):
                if numpy_array[i][j] > threshold:
                    numpy_array[i][j] = 255
                    Embroideryfile.moveLeft()
                else:
                    numpy_array[i][j] = 0
                    Embroideryfile.sewLeft()

        Embroideryfile.moveDown()

    return numpy_array


if __name__ == "__main__":

    Embroideryfile = JEF("Image_JEF_test.jef", 3, [1, 5, 6])

    filename = './Images/Black_Crown.jpg'
    targetPath = './Images/Crown_Binary.jpg'
    binary_image(filename, targetPath, 125)

    # File generation
    Embroideryfile.generatefile()


    