from JEF_class import JEF

# set up the embroidery file
jefName = "Square_Movement_by_JEF_Class.jef"
Embroideryfile = JEF(jefName)

for i in range(10):
    Embroideryfile.sewRight()
for i in range(10):
    Embroideryfile.moveRight()

for i in range(10):
    Embroideryfile.sewUp()
for i in range(10):
    Embroideryfile.moveUp()

for i in range(10):
    Embroideryfile.sewLeft()
for i in range(10):
    Embroideryfile.moveLeft()

for i in range(10):
    Embroideryfile.sewDown()
for i in range(10):
    Embroideryfile.moveDown()


##############################################################################################
# File generation
Embroideryfile.generatefile()