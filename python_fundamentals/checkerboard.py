def checkerboard(): #creates checkerboard pattern based on odds/evens and spacing of ***
    for i in range (0, 8):#will loop through these ranges
        if i % 2 == 0:
            print "* " * 4 #****
        elif i % 2 != 0:
            print " *" *4

print checkerboard()
