class Call(object):
    def __init__ (self, unique_id, name, phone, time, reason):
        self.unique_id = unique_id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        print self.unique_id
        print self.name
        print self.phone
        print self.time
        print self.reason

class Call_Center(object):
    def __init__ (self, calls):
        self.calls = []
        self.queue_size = self.queue_size()
    def add(self, add_call):
        self.calls.append(add_call)
        return self
    def remove(self, remove_call):
        self.calls.remove(remove_call)
        return self
    def queue_size(self):
        return len(self.calls)
    def info(self):
        for call in self.calls:
            call.display()

call_1 = Call(184, "sarah", "310-529-0788", "8:54", "help")
call_2 = Call(652, "lily", "555-468-8478", "8:55", "i'm hungry")
call_3 = Call(384, "stella", "127-766-5678", "8:59", "are you hungry?")

#call_3.display()

main_center = Call_Center([])
main_center.add(call_1).add(call_2).remove(call_2).add(call_3).info()
