def odd_even(): #counts through range and prints each iteration odd/even
    for i in range (1, 10):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        else:
            print "Number is " + str(i) + ". This is an odd number."
odd_even()

def multiply(list, multiplier): #iterates through each value in list and returns a list where each value has been multiplied by the multiplier
    new_list = []
    for i in list:
        new_list.append(i*multiplier)
    print new_list
multiply([2,4,10,16], 5)
