class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name) #super allows to modify parent (Animal) methods walk, run, display health
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
    def display_health(self): #super here allows us to combine the print statement with the rest of the method being the same as the parent display_health method
        print "This is a dragon"
        super(Dragon, self).display_health()

animal_1 = Animal("lily")
animal_1.walk().walk().walk().run().run().display_health()

animal_2 = Dog("chloe")
animal_2.walk().walk().walk().run().run().pet().display_health()

animal_3 = Dragon("stella")
animal_3.display_health()

animal_4 = Animal("munchkin") #This animal cannot call on pet, fly, or dragon's display_health, only the parent (Animal) methods
animal_4.display_health()
