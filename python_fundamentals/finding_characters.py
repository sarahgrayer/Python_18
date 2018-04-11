def findchar(word_list, char): #function takes list of strings containing a single character letter, and prints a new list of all the strings containing that character
    new_list = []

    for i in range (0, len(word_list)):
        if word_list[i].find(char) > 0: #at least one instance of the character letter in that index
            new_list.append(word_list[i])
    print new_list

this_list = ["hello","world","my","name","is","sarah"]

findchar(this_list, "r") #calling function and passing in the list and character
