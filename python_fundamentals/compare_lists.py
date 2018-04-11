def comparelists(list_one, list_two): #function compares two lists and prints a message depending on if they are identical or not
    if list_one == list_two:
        print "they match!"
    else:
        print "no match"

list_one = [16,5]
list_two = [1,2,5,6,5,3]

comparelists(list_one, list_two)

list_one = ['carrots', 'milk']
list_two = ['celery', 'bread', 'cream']

comparelists(list_one, list_two)

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

comparelists(list_one, list_two)
