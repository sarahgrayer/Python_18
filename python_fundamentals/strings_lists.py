#Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.index("day") #prints the position of the first instance of the word "day"
print words.replace("day", "month", 1) #new string created where word "day" is replaced by the word "month". 1 means just the first instance, without the one all instances of "day" would be replaced by "month".

#Min and Max
x = [2,54,-2,7,12,98]
print max(x) #prints max value in x
print min(x)

#First and Last
list = ["hello",2,54,-2,7,12,98,"world", "goodnight"]
print (list[0], list[len(list)-1]) #prints the first and last values in the list "list"

#New List
array = [19,2,54,-2,7,12,98,32,10,-3,6]
array.sort() #sorts list in ascending order
first_list = array[:len(array)/2] #splits list in half, first ends with index 5
second_list = array[len(array)/2:] #second begins after index 5
second_list.insert(0, first_list) #pushes the list created with the first half into index 0 of the second half list
print second_list
