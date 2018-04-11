#multiples
for i in range (1, 1000): #prints all the odd numbers from 1 to 1000
    if (i%2 != 0):
        print i

for i in range (5, 1000000): #prints all multiples of 5 from 5 to 1,000,000.
    if (i%5 == 0):
        print i

#Sum List
a = [1,2,5,10,255,3] #prints sum of values in list
print sum(a)

#Ave list
b = [1,2,5,10,255,3] #prints the average of the values in list
print sum(b)/len(b)
