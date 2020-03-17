from JEF_class import JEF

# set up the embroidery file
jefName = "text.jef"
Embroideryfile = JEF(jefName)


Embroideryfile.readText('Digital Manufacturing')

##############################################################################################
# File generation
Embroideryfile.generatefile()