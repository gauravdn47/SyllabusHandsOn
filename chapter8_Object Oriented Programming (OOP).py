# Writing a Student class
# Adding Laptop Reference in Student class and setting up interclass communication
# Writing a Laptop class

class Student:
    def __init__(self,first_name, last_name, laptop):
        self.first_name = first_name
        self.last_name = last_name
        self.laptop = laptop

    def stud(self):
        print(self.first_name+" "+self.last_name,"is studying.")

class Laptop:
    def __init__(self, model, price):
        pass

lap = Laptop(input("Enter Laptop name: "),input("Enter laptop price: "))

a = Student(input("Enter first_name:"),input("Enter last_name:"), lap)
a.stud()
