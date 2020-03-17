from JEF_class import JEF
from math import *

# set up the embroidery file
jefName = "Fractals.jef"
Embroideryfile = JEF(jefName)

##############################################################################################
# Spriograph fractal pattern

# control the step size
stepsize = 1
# stepsize = int(input("Enter the step size of the factal pattern: "))

# starting time
t = 0
# t = int(input("Enter the start step of the factal pattern: "))

# end time
t_end = 5000
# t_end = int(input("Enter the end step of the factal pattern (the higher the endtime, the more complex the pattern will be!): "))

# scale factor
scale = 10
# scale = int(input("Enter the Scaling factor of the factal pattern: "))

# propeties Parameters
R=8
# R = int(input("Enter the R parameter of the Spirograph pattern: "))

r=3
# r = int(input("Enter the r parameter of the Spirograph pattern: "))

a=3
# a = int(input("Enter the a parameter of the Spirograph pattern: "))

while t < t_end:
    x_axis = (R-r)*cos(r/R*t/scale)+a*cos((1-r/R)*t/scale)
    y_axis = (R-r)*sin(r/R*t/scale)-a*sin((1-r/R)*t/scale)

    Embroideryfile.customSew(x_axis, y_axis)
    t = t + stepsize

    if t % 1000 == 0:
        Embroideryfile.nextColor()


##############################################################################################
# File generation
Embroideryfile.generatefile()