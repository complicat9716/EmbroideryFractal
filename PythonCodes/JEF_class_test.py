from JEFclass import JEF
from math import *



# JEF(File_name, number_of_thread)     default 1 thread
Embroideryfile = JEF("fileClass_test.jef")



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