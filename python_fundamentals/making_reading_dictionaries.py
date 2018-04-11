me={}
me["name"]="Sarah"
me["age"]="28" #if this is an int rather than a string, need to change below to "str(data)" in order to concatenate
me["country of birth"]="USA"
me["favorite language"]="Python"

def my_info():
    for key, data in me.iteritems():
        print "My " + key + " is " + data 
my_info()
