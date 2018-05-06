
class Patient(object):
    PATIENT_COUNT = 1
    def __init__ (self, name, allergies):
        self.id = Patient.PATIENT_COUNT
        Patient.PATIENT_COUNT += 1
        self.name = name
        self.allergies = allergies
        self.bed_num = "none"

class Hospital(object):
    def __init__ (self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(100, (100 + (self.capacity))):
            beds.append({
                "bed_id": i,
                "available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) < self.capacity:
            #add to list of patients
            self.patients.append(patient)
            #if still capacity, incriment bed # and make last bed # unavailable
            for i in range(0, len(self.beds)):
                if self.beds[i]["available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["available"] = False
                    break
                    #print message
            print "{}, Patient #{}, was admitted to bed #{}".format(patient.name, patient.id, patient.bed_num)
            print "Allergies: "+ patient.allergies
            return self
        else:
            print "Sorry {}, hospital is full".format(patient.name)
            return self

    def discharge(self, patient_id): #pass patient_id here, best to identify this patient
        for patient in self.patients:
            if patient.id == patient_id:
            #make bed unavailable
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["available"] = True
                        break
                print "{} successfully discharged. Bed #{} is now available".format(patient.name, patient.bed_num)
                self.patients.remove(patient)
            else:
                print "Patient not found"
        return self

    def display(self):
        print "there are {} patients admitted to {}.".format(len(self.patients), self.name)

h1 = Hospital("Callaway", 2)
h2 = Hospital("Regional", 2)
p1 = Patient("Sarah", "none")
p2 = Patient("Justin", "bees")
p3 = Patient("Chloe", "chocolate")

#h1.admit(p1).admit(p2).discharge(1).admit(p3).display()
h1.admit(p3).discharge(8).discharge(3).admit(p2)
