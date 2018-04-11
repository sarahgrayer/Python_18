mixed_list = ['magical unicorns ',19,'hello ',98.98,'world ']
integer_list = [1,2,3,4,5]
string_list = ["spiff ", "moon ", "robot "]

def typelist(list): #each item in list is tested for its data type. If string, concatenate onto new string. If number, add to running sum.
    newstring = ""
    total = 0

    for element in list: #element is given variable name, could use "value", "i", etc.
        if isinstance(element, int) or isinstance(element, float): #add up each accurence that is int or float type element, which includes numbers that are decimals
            total = total + element
        elif isinstance (element, str): #concatenate each occurence that is a string type element
            newstring += element
    if newstring and total:
        print "This array has mixed value types."
        print newstring
        print total
    elif newstring:
        print "This array is all strings."
        print newstring
    else:
        print "This array is all numbers."
        print total


print typelist(mixed_list)#calls function typelist for "mixedlist"

print typelist(integer_list)

print typelist(string_list)
