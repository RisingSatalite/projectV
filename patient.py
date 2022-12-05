class Patient:
    patient_list = []
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def read(self):
        self.patient_list.clear()
        f = open("classes/patients.txt", "r")
        lines = f.readlines()
        for l in lines:
            inst = l.split("_")
            patientFile = Patient(inst[0], inst[1], inst[2], inst[3], inst[4])
            self.patient_list.append(patientFile)
        f.close()

    def print_data(self):
        for i in range(len(self.patient_list)):
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(self.patient_list[i].pid, self.patient_list[i].name, self.patient_list[i].disease, self.patient_list[i].gender, self.patient_list[i].age))
    
    def print_names(self):
        for i in range(len(self.patient_list)):
            print(self.patient_list[i].name)
    
    def add_patient(self, pid, name, disease, gender, age):
        f = open("classes/patients.txt", "a")
        f.write(f"\n{pid}_{name}_{disease}_{gender}_{age}")
        f.close()
    
    def write(self):
        f = open("classes/patients.txt", "w")
        f.seek(0)
        for i in range(len(self.patient_list)):
            f.write(f"{self.patient_list[i].pid}_{self.patient_list[i].name}_{self.patient_list[i].disease}_{self.patient_list[i].gender}_{self.patient_list[i].age}")
        f.close()
        Patient().read()
    
    def search_by_ID(self, ID):
        for i in range(len(self.patient_list)):
            if ID == self.patient_list[i].pid:
                print("Patient found")
                print(F"Patient name is {self.patient_list[i].name}")
                return(i)
        print("Not Found")
        return("Not Found")
    
    def print_info_by_ID(self, ID):
        i = Patient().search_by_ID(ID)
        if i == "Not Found":
            print("Can not find patient information")
        else:
            print((f"ID:{self.patient_list[i].pid}\nName:{self.patient_list[i].name}\nDisease:{self.patient_list[i].disease}\nGender:{self.patient_list[i].gender}\nAge:{self.patient_list[i].age}"))
    
    def edit_patient_by_ID(self, ID):
        i = Patient().search_by_ID(ID)
        if i != "Not Found":
            while True:
                edit = input("What to edit for the patient 'name' 'disease' 'gender' 'age' 'nothing'")
                match edit:
                    case "nothing":
                        break
                    case "name":
                        name2 = input("Enter new name")
                        self.patient_list[i].name = name2
                    case "disease":
                        disease2 = input("Enter new disease name")
                        self.patient_list[i].disease = disease2
                    case "disease":
                        gender2 = input("Enter new gender")
                        self.patient_list[i].gender = disease2
                    case "disease":
                        age2 = input("Enter new age")
                        self.patient_list[i].age = disease2
            Patient().write()
        else:
            print("Can not find patient information")

class Managment:
    while True:
        Patient().read()
        todo = input("What do you want to do 'write' 'print data' 'add patient' ")
        match todo:
            case "print data":
                Patient().print_data()
            case "print names":
                Patient().print_names()
            case "write":
                Patient().write()
            case "add patient":
                pid = input("Enter patient pid")
                name = input("Enter patient name")
                disease = input("Enter patient diease")
                gender = input("Enter patient gender")
                age = input("Enter patient age")
                Patient().add_patient(pid, name, disease, gender, age)
            case "Search ID":
                s_id = input("Enter the ID you want to check in the database")
                Patient().search_by_ID(s_id)
            case "Display by ID":
                s_id = input("Enter the ID for Patient to search")
                Patient().print_info_by_ID(s_id)
            case "Edit by ID":
                ID = input("Enter patient ID")
                Patient().edit_patient_by_ID(ID)
                print("Saving")

            case other:
                print("Unrecognized input")
