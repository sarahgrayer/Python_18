def draw_stars(list): #takes numbers and prints out corresponding # of stars
    for i in list:
        print "*" * i

draw_stars([4,6,1,3,5,7,25])

def modified_draw_stars(list): #when a string is passed, instead of displaying *'s, display the first letter of the string times the length of the string
    for i in list:
        if isinstance(i, int):
            print "*" * i
        else:
            print i[0] * (len(i))#letter in index 0

modified_draw_stars([4, "tom", 1, "michael", 5, 7, "jimmy smith"])
