def scores(tests): #generates "tests" (10) scores between 60 & 100. Display grade (A-D) for each score
    print "Scores and Grades"
    for i in range (0, tests):
        import random
        random_num = random.randint(60, 101) #.randint() returns integer, .random() returns a floating point between 0 and 1
        if random_num >= 90:
            print "Score:" + str(random_num) + "; Your grade is A!!!"
        elif random_num >= 80:
            print "Score:" + str(random_num) + "; Your grade is B"
        elif random_num >= 70:
            print "Score:" + str(random_num) + "; Your grade is C"
        else:
            print "Score:" + str(random_num) + "; Your grade is D"
    print "End of the program. Bye!"

scores(10)
