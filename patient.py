from person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID # public
        self._bloodGroup = bloodGroup # protected 
        self.__medicalHistory = medicalHistory # private

    def showInfo(self):
        print(f"Name:{self.name}\nSurname:{self.surname}\nPhone:{self.phone}")

    def getMedicalHistory(self):
        return self.__medicalHistory

    def updateMedicalHistory(self,newHistory):
        self.__medicalHistory = newHistory
        print("Medical history updated successfully!")