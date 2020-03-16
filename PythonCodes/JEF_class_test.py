from JEF_class import JEF


# User interface
print("############################################################################")
print("Welcome to the Fractal Pattern JEF file generator! :)")

print("############################################################################")
jefName = input("Enter a file name (please include (.jef)): ")
# jefName = "JEF_test_withEveryThing.jef"

print("############################################################################")
n_thread = int(input("Enter the number of threads: "))
# n_thread = 3

while True:
    print("############################################################################")
    color_list = list(int(num) for num in input("Input a list of color code (seperate by space): ").strip().split())
    if len(color_list) == n_thread:
        break
    else:
        print('the number of color didn\'t match the number of threads. Try again.')

# color_list = [1, 5, 6]

# JEF(File_name, number_of_thread, color_code_list)     default 1 thread and green color
Embroideryfile = JEF(jefName, n_thread, color_list)


################################
# File generation
Embroideryfile.generatefile()
print("############################################################################")
print('.JEF file generated successfully! Check your root folder! :)')