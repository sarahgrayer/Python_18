name = ["Anne,", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Sarah", "Justin"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "dog", "dolphins", "llamas"]

def makedict(arr1, arr2): #takes in two lists and creates a single dictionary as key/val pairs
    new_dict = dict(zip(arr1, arr2))
    print new_dict
makedict(name, favorite_animal)
