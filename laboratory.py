class Laboratory:
    laboratory_list = []
    def __init__(self, name="", cost=""):
        self.name = name
        self.cost = cost
    def read(self):
        f = open("classes/laboratories.txt", "r")
        lines = f.readlines()
        for l in lines:
            inst = l.split("_")
            labObject = Laboratory(inst[0], inst[1])
            self.laboratory_list.append(labObject)
        f.close()
    def write(self):
        f = open("classes/laboratories.txt", "w")
        f.seek(0)
        for i in range(len(self.laboratory_list)):
            f.write(f"{self.laboratory_list[i].name}_{self.laboratory_list[i].cost}")
        f.close()
        Laboratory.read(self)
    def print_data(self):
        for i in range(len(self.laboratory_list)):
            print("{:<15} {:<15}".format(self.laboratory_list[i].name, self.laboratory_list[i].cost))
    def print_lab_names(self):
        for i in range(len(self.laboratory_list)):
            print(self.laboratory_list[i].name)
    def new_object(self, name, cost):
        labObject = Laboratory(name, cost)
        self.laboratory_list.append(labObject)
        f = open("classes/laboratories.txt", "a")
        f.write(f"\n{name}_{cost}")
        f.close()

class Managment:
    while True:
        #read inital read the data
        #lab names print names of all labs
        #add creates a new object and adds it to the laboratories.txt file
        #print takes data and print in nice format
        #write from the data, it write it on the laboratories.txt file
        do = input("What do you want to do 'write' 'print' 'add' 'lab names'")
        Laboratory().read()
        match do:
            case "write":
                Laboratory().write()
            case "print":
                Laboratory().print_data()
            case "lab names":
                Laboratory().print_lab_names()
            case "add":
                name = input("Enter lab name ")
                cost = input("Enter lab cost ")
                Laboratory().new_object(name, cost)
            case other:
                print("Unrecognized input")