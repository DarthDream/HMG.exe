from doctor import Doctor
from patient import Patient
from hospital import Hospital

hospital = Hospital("My Library")

def menu():
    print(f'''

     =========== HOSPITAL.EXE ===========
        1. Add Doctor
        2. Add Patient
        3. Show All Doctors
        4. Show All Patients
        5. Create Appointment
        6. Show All Appointments
            0. Exit


    ''')

def app():
  try:
    while True:
        choice=input("Secim et:")
        if choice=="1":
            DoctorName=input("Ad daxil et:")
            DoctorID=int(input("Ad daxil et:"))
            DoctorPhone=int(input("Ad daxil et:"))

            doctor =Doctor(DoctorName,DoctorID,DoctorPhone)
            hospital.addDoctor(doctor)

        elif choice=="2":
            PatientName=input("Ad daxil et:")
            PatientID=int(input("Ad daxil et:"))
            PatientPhone=int(input("Ad daxil et:"))

            patient =Patient(PatientName,PatientID,PatientPhone)
            hospital.addPatient(patient)

        elif choice=="3":
            hospital.showDoctors()

        elif choice=="4":
            hospital.showPatients()

        elif choice=="5":
            Date=int(input("Vaxt daxil et:"))
            AppointmentID=int(input("ID daxil et:"))
            Appointment=input("Rezerv daxil et:")
            DoctorName=input("Ad daxil et:")

            appointment=(Date,AppointmentID,Appointment)
            hospital.createAppointment(appointment)

        elif choice=="6":
            hospital.showAppointments()

        elif choice=="0":
            print("Exit...")
            break

        else:
            print("404")
            continue
  except:
      print("404")