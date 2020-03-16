from JEF_class import JEF


# JEF(File_name, number_of_thread)     default 1 thread
Embroideryfile = JEF("Final_Product.jef")

Embroideryfile.customMove(200, 200)

################################
# File generation
Embroideryfile.generatefile()