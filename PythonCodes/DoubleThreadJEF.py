
Num_thread = 4


##################################################################################################
# Start first stitch


stitches0 = [128, 2,
            0, 0,
	        0, 0,]

# Middle steps
for i in range(0, 10):    
    stitches0 += [246, 0,]
for i in range(0, 10):    
    stitches0 += [0, 246,]


##################################################################################################
# Start second stitch

stitches1 = [128, 1,
            128, 2,
            0, 0,]

# Middle steps
for i in range(0, 10):    
    stitches1 += [246, 0,]
for i in range(0, 10):    
    stitches1 += [0, 246,]


##################################################################################################
# Start third stitch

stitches2 = [128, 1,
            128, 2,
	        0, 0,]

# Middle steps
for i in range(0, 10):    
    stitches2 += [246, 0,]
for i in range(0, 10):    
    stitches2 += [0, 246,]


##################################################################################################
# Start fourth stitch

stitches3 = [128, 1,
            128, 2,
	        0, 0,]

# Middle steps
for i in range(0, 10):    
    stitches3 += [246, 0,]
for i in range(0, 10):    
    stitches3 += [0, 246,]
  

##################################################################################################
# Prepare the JEF file

# Combine stitches
stitches = stitches0 + stitches1 + stitches2 + stitches3

# "Last stitch" command code
stitches +=  [128, 16] 

# Header of the JEF files
jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
            10, 0, 0, 0,    # Unknown number
            ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
            ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
            ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0,  # SS00
            Num_thread, 0, 0, 0,     # Number of physical threads (1)
            ((len(stitches))//2) & 0xff, 0, 0, 0,     # Number of stitches
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
            ] + stitches


jefBytes = bytes(jefBytes)
with open("Square_test.jef", "wb") as f:
    f.write(jefBytes)