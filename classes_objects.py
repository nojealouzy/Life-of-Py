class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started working.")


#creating objects

car1 = Car("Toyota","Corolla")
car2 = Car("Tesla","Model 3")

car1.start_engine()
car2.start_engine()



#Task1: Creating a book class

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print(f"{self.author}'s book name is {self.title}.")

book1 = Book("naa save nen sastha","koushi")

book1.display()



#Homework - create a student class with name, roll number, method to display details

class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number

    def gate_selected_profiles(self):
        print(f"{self.name} of roll number {self.roll_number} is selected.")

#creating objects

student1 = Student("Confusion Matrix",'123nc10')

student1.gate_selected_profiles()



#Task3 - Planet class

class Planet:
    def __init__(self,name,closest,farthest):
        self.name = name
        self.closest = closest
        self.farthest = farthest

    def Planet_details(self):
        print(f"{self.name}'s closest planet is {self.closest}.")
        print(f"{self.name}'s farthest planet is {self.farthest}.")

planet1 = Planet('Earth','Mars','Saturn')

planet1.Planet_details()




#Task4 - Phone class

class Phone:
    def __init__(self,brand_model,battery,ram):
        self.brand_model = brand_model
        self.battery = battery
        self.ram = ram

    def phone_specifications(self):
        print(f"{self.Brand_model}'s battery is {self.Battery} mah and has {self.Ram} gb of Ram.")

phone1 = Phone("Iphone 16 Pro",6000, 128)

phone1.Phone_specifications()