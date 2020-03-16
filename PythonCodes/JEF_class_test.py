from JEFclass import JEF
from math import *


# JEF(File_name, number_of_thread)     default 1 thread
Embroideryfile = JEF("JEF_test.jef")



for i in range(0, 10):  
    Embroideryfile.sewRight()


Embroideryfile.trimSew()

Embroideryfile.moveThread(100, 100)


for i in range(0, 10):  
    Embroideryfile.sewDown()

# File generation
Embroideryfile.generatefile()