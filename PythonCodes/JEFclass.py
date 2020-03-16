# JEF class for controlling the Embroidery pattern
class JEF():

    # initialize the pattern with 1mm offset in both x and y
    def __init__(self, fileName, nThread = 1):
        self.jefBytes = None
        self.stitches = [128, 2,
                        0, 0,
                        10, 10,]
        self.fileName = fileName
        self.nThread = nThread

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

    # trim the wire and move to the specified location
    def moveThread(self,  x_axis, y_axis):
        self.stitches += [128, 2,
                         0, 0,]
        customSew(x_axis, y_axis)

    # change to the next thread color in system
    def nextColor(self):
        self.stitches += [128, 1,
                         0, 0,
                         0, 0,]

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

    # testing zig zag
    def zigZag(self, step):
        x_axis = 10*sin(step)
        y_axis = step

        theta = pi/3

        # 2D rotation
        x_axis_new = cos(theta)*x_axis - sin(theta)*x_axis
        y_axis_new = sin(theta)*x_axis + cos(theta)*x_axis

        self.customSew(x_axis_new, y_axis)
        
    # generate the JEF file
    def generatefile(self):

        self.stitches +=  [128, 16] 

        self.jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
                        10, 0, 0, 0,    # Unknown number
                        ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
                        ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
                        ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
                        ord("0"), ord("0"), 99, 0,  # SS00
                        self.nThread, 0, 0, 0,     # Number of physical threads (1)
                        ((len(self.stitches))//2) & 0xff, 0, 0, 0,     # Number of stitches
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
                        3, 0, 0, 0,    # Thread color
                        4, 0, 0, 0,    
                        5, 0, 0, 0,
                        6, 0, 0, 0,
                        ] + self.stitches

        # Convert bytes
        self.jefBytes = bytes(self.jefBytes)

        # write file
        with open(self.fileName, "wb") as f:
            f.write(self.jefBytes)



# Test unit
if __name__ == "__main__":

    from math import *

    # JEF(File_name, number_of_thread)     default 1 thread
    Embroideryfile = JEF("fileClass_test.jef")

    for i in range(0, 10):  
        Embroideryfile.sewRight()
    
    Embroideryfile.nextColor()

    for i in range(0, 10):  
        Embroideryfile.sewDown()

    Embroideryfile.nextColor()

    for i in range(0, 10):  
        Embroideryfile.sewLeft()

    Embroideryfile.nextColor()

    for i in range(0, 10):  
        Embroideryfile.sewUp()

    ################################
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

    ################################
    #zig-zag test
    for i in range(20):
        Embroideryfile.zigZag(i)

    ################################
    #circle 

    # control the step size
    stepsize = 0.1

    # starting point
    t = 0

    # end point
    end = 2*pi

    while t < end:
        x_axis = scale*cos(t)
        y_axis = scale*sin(t)

        Embroideryfile.customSew(x_axis, y_axis)
        t = t + stepsize

    ################################
    # File generation
    Embroideryfile.generatefile()
