from appointment import Appointment

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctor(self, doctor):
        self.doctors.append(doctor)

    def addPatient(self, patient):
        self.patients(patient)

    def showDoctors(self):
        return self.doctors

    def showPatients(self):
        return self.patients

    def createAppointment(self, doctorID, patientID, date):
        self.appointments(doctorID,patientID,date)

    def showAppointments(self):
        return self.appointments