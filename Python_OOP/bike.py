class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price: $" + str(self.price)
        print "Max speed: " + str(self.max_speed) + " mph"
        print "Total miles: " + str(self.miles) + " miles"

    def ride(self):
        print "riding"
        self.miles += 10
        return self

    def reverse(self):
        print "reversing"
        if self.miles > 5:
            self.miles -= 5
        return self

bike1 = Bike(49, "25mph")
bike2 = Bike(99, "35mph")
bike3 = Bike(199, "50mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
