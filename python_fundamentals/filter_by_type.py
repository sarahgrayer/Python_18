sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

i = spL
vartype = type(i)

#first test what type of variable i is with type(i), then run if statements. int, str, and list are built in.
if vartype is int:
    if i >= 100:
        print "That's a big number!"
    else:
        print "That's a smaller number!"
elif vartype is str:
    if len(i) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"
elif isinstance(i, list): #lenth of list
    if len(i) >= 10:
        print "Big list!"
    else:
        print "Short list!"
