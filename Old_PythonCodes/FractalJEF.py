from math import *

##################################################################################################
# 

stitches = [128, 2,
	        0, 0,
            206, 206,]

# control the step size
stepsize = 1

# starting time
t = 0

# end time
t_end = 5000

# scale factor
scale = 10

# Parameters
R=5
r=1.08
a=3


while t < t_end:

    ################################
    # x_axis
    x_axis = int((R-r)*cos(r/R*t/scale)+a*cos((1-r/R)*t/scale))

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
    y_axis = int((R-r)*sin(r/R*t/scale)-a*sin((1-r/R)*t/scale))

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

    if t % 1000 == 0:
        stitches += [128, 1,
                    128, 2,
                    0, 0,]

stitches +=  [128, 16]         # "Last stitch" command code

##################################################################################################


jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
            10, 0, 0, 0,    # Unknown number
            ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
            ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
            ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0,  # SS00
            1, 0, 0, 0,     # Number of physical threads (1)
            (len(stitches)//2) & 0xff, 0, 0, 0,     # Number of stitches
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
            10, 0, 0, 0,    # Thread color
            ] + stitches
 

jefBytes = bytes(jefBytes)
with open("Fractal_test.jef", "wb") as f:
    f.write(jefBytes)
