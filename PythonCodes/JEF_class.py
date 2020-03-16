# JEF class for controlling the Embroidery pattern
class JEF():

    # initialize the pattern with 1mm offset in both x and y
    def __init__(self, fileName, nThread = 1, color_list = [6]):
        self.jefBytes = None            # empty file
        self.stitches = [128, 2,
                        0, 0,
                        10, 10,]        # start with an offset 1mm, 1mm
        self.fileName = fileName        # store the file name
        self.nThread = nThread          # number of threads
        self.colorINFO = []             # color info

        # store the color information
        for i in range(nThread):
            self.colorINFO += [color_list[i], 0, 0, 0,]

        # print(self.colorINFO)

    ##############################################################################
    # Sew functions

    # sew left 1mm
    def sewLeft(self):
        self.stitches += [246, 0,]

    # sew right 1mm
    def sewRight(self):
        self.stitches += [10, 0,]

    # sew up 1mm
    def sewUp(self):
        self.stitches += [0, 10,]

    # sew down 1mm
    def sewDown(self):
        self.stitches += [0, 246,]

    # user custom sew locations (with validate methods)
    def customSew(self, x_axis, y_axis):

        x_axis = int(x_axis)
        y_axis = int(y_axis)

        # Positive limit
        if x_axis > 127:
            print("X positive limit exceed!!")

        if x_axis < 0:
            x_axis = 256 + x_axis

            # negative limit
            if x_axis < 129:
                print("X negative limit exceed!!")


        # Positive limit
        if y_axis > 127:
            print("Y positive limit exceed!!")

        if y_axis < 0:
            y_axis = 256 + y_axis

            # negative limit
            if y_axis < 129:
                print("Y negative limit exceed!!")
                
        self.stitches += [x_axis, y_axis,]

    ##############################################################################
    # Movement functions

    # trim the thread
    def trimThread(self):
        self.stitches += [128, 2,
                         0, 0,]

    # move left by 1mm
    def moveLeft(self):
        self.trimThread()
        self.stitches += [246, 0,]

    # move right by 1mm
    def moveRight(self):
        self.trimThread()
        self.stitches += [10, 0,]

    # move up by 1mm
    def moveUp(self):
        self.trimThread()
        self.stitches += [0, 10,]

    # move down by 1mm
    def moveDown(self):
        self.trimThread()
        self.stitches += [0, 246,]

    # trim the wire and move to the specified location
    def customMove(self,  x_axis, y_axis):
        self.trimThread()
        self.customSew(x_axis, y_axis)

    # change to the next thread color in system
    def nextColor(self):
        self.stitches += [128, 1,
                         0, 0,
                         0, 0,]

    ##############################################################################
    # Other functions

    # testing zig zag
    def zigZag(self, flag):
        x_axis = ((-1)**flag) * (10)
        y_axis = 10

        self.customSew(x_axis, y_axis)

    ##############################################################################
    # image processing

    # read image
    def readImage(self, img_path, threshold):
        # load image
        image_file = Image.open(img_path)

        # convert image to light intensity
        image = image_file.convert('L')
        image = numpy.array(image)

        # binarlize image
        image = self.binarize_array(image, threshold)

        # show gray scale image
        plt.gray()
        plt.imshow(image)

        # print(image.shape)

        # show the plot
        plt.show()

    def binarize_array(self, numpy_array, threshold = 200):
        # for each row
        for i in range(len(numpy_array)):

            # if it is a even row
            if i%2 == 0:

                # read the image from left to right
                for j in range(len(numpy_array[0])):

                    # if there is a black pixel make a stitch, else move the same distance
                    if numpy_array[i][j] > threshold:
                        numpy_array[i][j] = 255
                        self.moveRight()
                    else:
                        numpy_array[i][j] = 0
                        self.sewRight()

            # if it is a odd row
            else:

                # read the image from right to left
                for j in reversed(range(len(numpy_array[0]))):

                    # if there is a black pixel make a stitch, else move the same distance
                    if numpy_array[i][j] > threshold:
                        numpy_array[i][j] = 255
                        self.moveLeft()
                    else:
                        numpy_array[i][j] = 0
                        self.sewLeft()

            # move the thread down after each row
            self.moveDown()

        return numpy_array
        
    ##############################################################################
    # generate the JEF file
    def generatefile(self):

        self.stitches +=  [128, 16] 

        self.jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
                        10, 0, 0, 0,    # Unknown number
                        ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
                        ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
                        ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
                        ord("0"), ord("0"), 99, 0,  # SS00
                        self.nThread, 0, 0, 0,     # Number of physical threads
                        0, 0, 0, 0,     # Number of stitches
                        3, 0, 0, 0,     # Sewing machine hoop             
                        50, 0, 0, 0,    # Left boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Top boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Right boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Bottom boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Left boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Top boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Right boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Bottom boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Left boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Top boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Right boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Bottom boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Left boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Top boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Right boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Bottom boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Left boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Top boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Right boundary distance from center (in 0.1 mm)
                        50, 0, 0, 0,    # Bottom boundary distance from center (in 0.1 mm)
                        ] + self.colorINFO + self.stitches

        # print(self.colorINFO + self.stitches)

        # Convert bytes
        self.jefBytes = bytes(self.jefBytes)

        # write file
        with open(self.fileName, "wb") as f:
            f.write(self.jefBytes)


#########################################################################################
# Test unit
if __name__ == "__main__":

    from math import *
    import numpy
    from PIL import Image
    import cv2
    import matplotlib.pyplot as plt

   # The jef file only accepts 3 colors 
    # JEF(File_name, number_of_thread, color_code_list)     default 1 thread and green color
    Embroideryfile = JEF("JEF_test_withEveryThing.jef", 3, [1, 5, 6])

    #############################################################################################
    # read a user specified image, take 125 as the threshold (show user the processed image)
    filename = './Images/CU_VerySmall.png'
    Embroideryfile.readImage(filename, 125)

    #############################################################################################
    # displacement
    Embroideryfile.customMove(120, -60)
    Embroideryfile.customMove(110, 0)

    ##############################################################################################
    # fractal pattern

    # control the step size
    stepsize = 1

    # starting time
    t = 0

    # end time
    t_end = 5000

    # scale factor
    scale = 10

    # Parameters
    R=7
    r=1.08
    a=4

    while t < t_end:
        x_axis = (R-r)*cos(r/R*t/scale)+a*cos((1-r/R)*t/scale)
        y_axis = (R-r)*sin(r/R*t/scale)-a*sin((1-r/R)*t/scale)

        Embroideryfile.customSew(x_axis, y_axis)
        t = t + stepsize

        if t % 1000 == 0:
            Embroideryfile.nextColor()

    #############################################################################################
    # displacement
    Embroideryfile.customMove(120, 0)
    Embroideryfile.customMove(110, 0)

    ##############################################################################################
    # zig zag
    for i in range(100):
        Embroideryfile.zigZag(i)

    ##############################################################################################
    # File generation
    Embroideryfile.generatefile()