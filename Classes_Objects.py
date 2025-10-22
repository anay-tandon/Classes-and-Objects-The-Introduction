class Student():
    #properties/ attributes
    name = " "
    age = 12
    schoolclass = "6th A"
    house = "Sapphire"
    classteacher = "Shivani"

    #constructor
    def __init__(self):
        print("Making a new student")

    #Another Function
    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print("Please enter the name of the Student: ")
        self.name = input()

    #Another Function
    def show_Details(self):
        print("The details of students are:")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.classteacher)


anay = Student() #The Object
anay.change_details()
anay.show_Details()

siya = Student() #The Object
