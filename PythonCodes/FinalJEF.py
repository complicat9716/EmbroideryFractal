# Start stitch
stitches = [128, 2,
	    0, 0,
            206, 206,]

# Middle steps
for i in range(0, 10):    
    stitches += [10, 0,]
for i in range(0, 10):    
    stitches += [0, 10,]
for i in range(0, 10):    
    stitches += [246, 0,]
for i in range(0, 10):    
    stitches += [0, 246,]

# "Last stitch" command code
stitches +=  [128, 16]         



##################################################################################################
# Prepare the JEF file

# stitches = stitches1 + stitches2

# Header of the JEF files
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
            32, 0, 0, 0,         # Thread color (white)
            13, 0, 0, 0,        # Unknown number
            ] + stitches


jefBytes = bytes(jefBytes)
with open("Square_test.jef", "wb") as f:
    f.write(jefBytes)