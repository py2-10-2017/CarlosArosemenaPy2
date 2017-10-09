class patient(object):
    patientId = 0
    def __init__(self, name, allergies, *bedNo):
        patient.patientId += 1
        self.patientId = patient.patientId
        self.name = name
        self.allergies = allergies
        if bedNo:
            for bed in bedNo:
                self.bedNo = bed
        else:
            self.bedNo = None
