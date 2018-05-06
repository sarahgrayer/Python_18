class MathDojo(object):
    def __init__ (self):
        self.result = 0

    def add(self, *args):
        for i in args:
            if type (i) == list or type (i) == tuple: #add up everything in list/tuple
                for k in i:
                    self.result += k
            else:
                self.result += i
        #print self.result
        return self #have to return self in order to chain

    def subtract(self, *args):
        for i in args:
            if type(i) == list or type (i) == tuple:
                for k in i:
                    self.result -= k
            else:
                self.result -= i
        #print self.result
        return self

    def total(self):
        print self.result


md = MathDojo()
#md.add(210, 5).subtract(100).total()
md.add(2).add([2,5], 1).subtract(3,2).total()
