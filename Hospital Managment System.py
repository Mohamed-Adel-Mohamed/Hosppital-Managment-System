class Hospital:
    def __init__(self):
        self.list_of_patients = [[] for _ in range(20)]

    def prDisplay(self):
        print("                               Program Options:")
        print("                               1) Add new patient")
        print("                               2) Print all patients")
        print("                               3) Get next patient")
        print("                               4) Remove a leaving patient")
        print("                               5) End the program")
        print("Enter your choice from (1 to 5): ")
    def checkSpecialization(self,specialization):
            if len(self.list_of_patients[specialization-1])>10:
                print("Specialization is full \n")
            else:
                print("Enter patient name: ")
                patientName = input()
                print("Enter patient status (0 normal/ 1 urgent/ 2 super urgent): ")
                status = int(input())
                patient.addPatient(specialization, patientName,status)
                print("Patient:", patientName, "  Has been added to specialization:",specialization,"  With status:",status ,"\n")

    def addPatient(self,specialization,patientName,status):
        if status == 0:
            self.list_of_patients[specialization - 1].append({"patientName": patientName, "status": status})
        elif status == 1:
            for i, patient in enumerate(self.list_of_patients[specialization - 1]):
                if patient["status"] == 0:
                    self.list_of_patients[specialization - 1].insert(i + 1, {"patientName": patientName, "status": status})
                    break
            else:
                self.list_of_patients[specialization - 1].append({"patientName": patientName, "status": status})
        elif status == 2:
            for i, patient in enumerate(self.list_of_patients[specialization - 1]):
                if patient["status"] == 1 or patient["status"] == 0:
                    self.list_of_patients[specialization - 1].insert(i + 1, {"patientName": patientName, "status": status})
                    break
            else:
                self.list_of_patients[specialization - 1].append({"patientName": patientName, "status": status})
 
def printList(self, specialization):
        if len(self.list_of_patients[specialization - 1]) != 0:
            sorted_list = sorted(self.list_of_patients[specialization - 1],      key=lambda p: p['status'])
            for patient in sorted_list:
                if patient["status"] == 0:
                    print(patient["patientName"]," is normal" )
                elif patient["status"] == 1:
                    print(patient["patientName"], " is urgent")
                elif patient["status"] == 2:
                     print(patient["patientName"]," is super urgent" )
        else:
            print("Specialization is empty.")

def drcheck(self,specialization):
            if len(self.list_of_patients[specialization-1])==0:
                print("There are no patients, have a rest Doc.")
            else:
                print(self.list_of_patients[specialization-1][0],", Please go with the Doc.")
                self.list_of_patients[specialization-1].pop(0)

def removePatient(self, specialization, patientName):
        for patient in self.list_of_patients[specialization - 1]:
            if patient['patientName'].lower() == patientName.lower():
                self.list_of_patients[specialization - 1].remove(patient)
                print(patientName, "has been removed \n")
                return
        print("Patient is not found")


patient = Hospital()
patient.prDisplay()
choice=int(input())

while(choice!=5):
    if choice==1:
        print("Enter specialization Number: ")
        specialization = int(input())
        patient.checkSpecialization(specialization)

    if choice==2:
        print("Enter specilization: ")
        specialization=int(input())
        patient.printList(specialization)

    if choice==3:
        print("Enter specilization: ")
        specialization=int(input())
        patient.drcheck(specialization)

    if choice==4:
        print("Enter specialization: ")
        specialization=int(input())
        patientName= input("Enter patient name: ").strip().capitalize()
        patient.removePatient(specialization,patientName)

    patient.prDisplay()
    choice=int(input())

print("Program ended")