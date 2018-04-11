def coin_toss(num_tosses):
    print "Beginning the program"
    heads = 0#set variables before for loop begins, otherwise, if inside loop, would be re-set to 0 each time.
    tails = 0
    for i in range (1, num_tosses+1):
        import random
        random_num = random.randint(0, 1)
        if random_num == 0:
            heads = heads + 1
            print "Attempt " + str(i) + ": Throwing coin... It's a head!... Got", heads, "heads so far and", tails, "tails."#using commas to seperate requires just variable name, no extra spaces needed in surrounding string
        else:
            tails = tails + 1
            print "Attempt " + str(i) + ": Throwing coin... It's a tail!... Got " + str(heads) + " heads so far and " + str(tails) + " tails."#concatenating requires + str(variable), and extra spaces in strings. Both work.
    print "Ending the program"
coin_toss(10)

def coin_toss(num_tosses):
    heads = 0#set variables before for loop begins, otherwise, if inside loop, would be re-set to 0 each time.
    tails = 0
    for i in range (1, num_tosses+1):
        import random
        random_num = random.random() #produces random float 0 to 1
        toss = round(random_num) #rounds, to 0 or 1
        if toss == 0:
            heads = heads + 1
            print "Attempt " + str(i) + ": Throwing coin... It's a head!... Got", heads, "heads so far and", tails, "tails."#using commas to seperate requires just variable name, no extra spaces needed in surrounding string
        else:
            tails = tails + 1
            print "Attempt " + str(i) + ": Throwing coin... It's a tail!... Got " + str(heads) + " heads so far and " + str(tails) + " tails."#concatenating requires + str(variable), and extra spaces in strings. Both work.
coin_toss(10)
