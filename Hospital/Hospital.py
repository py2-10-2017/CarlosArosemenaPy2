from Patient import patient

class hospital(object):
    patients = []
    def __init__(self,hospName,capacity):
        self.patients = hospital.patients
        self.hospName = hospName
        self.capacity = capacity

    def admit_patient(self,name,allergies, *bedNo):

        if len(name)<1:
            return "Please insert a name"

        if len(allergies)<1:
            return "Please describe allergies, if none, just type 'N/A'"

        if bedNo:
            for bed in bedNo:
                self.bedNo = bed
        else:
            self.bedNo = None

        hospPatient = patient(name,allergies,bedNo)
        
