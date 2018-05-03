class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.tax = tax
        self.price = self.price + self.price * tax
        print "Price with tax: $" + str(self.price)
        return self
    def return_item(self, condition):
        self.condition = condition
        if self.condition == "defective":
            self.status = "defective"
            self.price = 0
        if self.condition == "like_new":
            self.status = "for sale"
        if self.condition == "opened":
            self.status = "used"
            self.price = (self.price * .80)
        else:
            print "invalid condition"
        return self
    def display_info(self):
        print "Price: $" + str(self.price)
        print "Name: " + self.name
        print "Weight: " + self.weight
        print "Brand: " + self.brand
        print "Status: " + self.status
        print "*******************"

item1 = Product(100, "mat", "2lb", "Sol")
item2 = Product(100, "mat", "2lb", "Sol")

item1.return_item("opened").display_info()
item2.add_tax(.10)
