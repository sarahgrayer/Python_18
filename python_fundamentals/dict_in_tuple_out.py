mydict = {
"Speros": "(555)555-5555",
"Michael": "(999)999-9999",
"Jay": "(777)777-7777"
}

def dictionary_list(): #prints 3 lists with the key/val pairs as the data (for loop)
    print "separate lists with key/val pairs as the data:"
    for key, value in mydict.iteritems():
        dictlist = ([key, value])
        print dictlist
dictionary_list()

def tuple(): #prints one list with the key/val pairs as tuples
    print "tuple list:"
    #mydict.items()
    #tuplelist = [(key, value) for key, value in mydict.iteritems()]
    for key, value in mydict.iteritems():
        tuplelist = [(key, value)]
    print tuplelist
tuple()
