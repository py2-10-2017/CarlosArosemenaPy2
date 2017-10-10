from Patient import patient

class hospital(object):
    patients = []
    def __init__(self,hospName,capacity):
        self.patients = hospital.patients
        self.hospName = hospName
        self.capacity = capacity

    def patient_count(self):
        if len(self.patients) >0:
            for patient in self.patients:
                print "Patient Id: "+str(patient.patientId)
                print "Patient Name: "+str(patient.name)
                print "Patient allergies: "+patient.allergies
                print "Bed Number: "+str(patient.bedNo)
                print "======================================"

        return self

    def admit_patient(self,name,allergies, *bedNo):
        if self.capacity > 0:

            hospPatient = patient(name,allergies,*bedNo)
            self.patients.append(hospPatient)

            self.capacity -= 1
        else:
            print "No more capacity"

        return self

    def discharge_patient(self,name):

        if self.patients:
            for patient in self.patients:
                if name == patient.name:
                    self.patients.pop(self.patients.index(patient))
                    self.capacity += 1
                else:
                    print "Patient name not in list"
        else:
            print "No patients to remove"

        return self


hosp = hospital("arohosp",2)

hosp.admit_patient('gato','gato allergies', 246).admit_patient('Carlos','carlos allergies').discharge_patient('gato').admit_patient('Carl','carl allergies', 248).patient_count()
