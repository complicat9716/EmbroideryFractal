from math import *

# Going through all four sides of the square
# Clockwise, starting at the bottom left
# Sides are 1 cm long, in ten stiches 1mm each
# 246 is the unsigned 8-bit version of -10


##################################################################################################

# Starting stitch
stitches = [128, 2,
	    0, 0,
            206, 206,]

# control the step size
stepsize = 0.1

# starting point
t = 0

# end point
end = 2*pi

# scale factor
scale = 10

while t < end:

    ################################
    # x_axis
    x_axis = int(scale*cos(t))

    # Positive limit
    if x_axis > 127:
        print("X positive limit exceed!!")

    if x_axis < 0:
        x_axis = 256 + x_axis

        # negative limit
        if x_axis < 129:
            print("X negative limit exceed!!")

    ################################
    # y_axis
    y_axis = int(scale*sin(t))

    # Positive limit
    if y_axis > 127:
        print("Y positive limit exceed!!")

    if y_axis < 0:
        y_axis = 256 + y_axis

        # negative limit
        if y_axis < 129:
            print("Y negative limit exceed!!")

    ################################
    # stitch
    stitches += [x_axis, y_axis,]
    t = t + stepsize

stitches +=  [128, 16]         # "Last stitch" command code

##################################################################################################

# jef headers
jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
            10, 0, 0, 0,    # Unknown number
            ord("2"), ord("0"), ord("2"), ord("0"), # YYYY
            ord("0"), ord("3"), ord("1"), ord("1"), # MMDD
            ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0,  # SS00
            1, 0, 0, 0,     # Number of physical threads (1)
            (len(stitches)//2) & 0xff, (len(stitches)//2) >> 8 & 0xff, 0, 0,     # Number of stitches
            3, 0, 0, 0,     # Sewing machine hoop             
			50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            32, 0, 0, 0,         # Thread color (orange)
            13, 0, 0, 0,        # Unknown number
            ] + stitches
 
# write jef file
jefBytes = bytes(jefBytes)
with open("Circle_test.jef", "wb") as f:
    f.write(jefBytes)
