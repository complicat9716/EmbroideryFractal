import numpy
from PIL import Image
import cv2
import matplotlib.pyplot as plt


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

    # show histogram
    plt.figure()
    plt.hist(image.flatten())

    plt.show()

    # save image
    cv2.imwrite(targetPath, image)

# loop through the image array
def binarize_array(numpy_array, threshold = 200):
    # for each row
    for i in range(len(numpy_array)):
        #for each column
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


if __name__ == "__main__":
    filename = './Images/CU_circle.png'
    targetPath = './Images/Binary.jpg'
    binary_image(filename, targetPath, 125)
