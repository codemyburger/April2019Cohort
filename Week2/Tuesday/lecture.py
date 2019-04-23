

# student1 = "Tarkek"
# student2 = "Chris"
# student3 = "Michael"


# def Students():
#     print(f"{student1} {student2} {student3}")


# Students()

# student1 = "Glen"

# Students()


# class Students:

#     def PrintStudents():
#         print("Tarek Chris Michael")
#Students.PrintStudents()

# class Students:

#     def students(self):
#         print("Tarek Chris Michael")

# Michael = Students()
# Michael.students()

# Chris = Students()
# Chris.students()

# class MyClass(object):
#     def __init__(self, first_name, last_name):
#         print("hello world")
#         self.first_name = first_name
#         self.last_name = last_name

#     def printName(self):
#         # name = "Celeste"
#         print(f"{self.first_name} {self.last_name} ")


# dc = MyClass("Chris", "Humphrey")
# dc.printName()

# dc_houston = MyClass("Mohammad", "Azam")
# dc_houston.printName()


# def Person(name, count):
    
#     print(f"my name is {name} {count}")
#     count = count + 1
#     return count



# count = Person("Lisa", 0)
# print(count)

# count = 67
# count = Person("Veronica", count)
# print(count)


# countPeter = Person("Peter", 5)
# print(countPeter)
# countPeter = Person("Bob", countPeter)
# print(countPeter)

# Cindy = Person("Cindy")


# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         self.count = 0 
#         print(f"my name is {self.name}")

#     def change_name(new_name):
#         self.count = self.count + 1
#         self.name = new_name
#         print(f"name is {self.name} I've changed my name {self.count} times")
    

# class Person(object):
#     def __init__(self, name, whoAmI):
#         self.name = name
#         self.count = 0
#         self.whoAmI = whoAmI
#         # print(f"hello {self.name}")


#     def change_name(self, new_name):
#         self.name = new_name
#         self.count = self.count + 1
#         print(f"who: {self.whoAmI} name:{self.name} count: {self.count}")


# student = Person("veronica", "student")
# atlanta_student = Person("Michael", "atlanta_student")

# student.change_name("Matt")
# student.change_name("Katy")
# student.change_name("Chris")
# atlanta_student.change_name("Jake")



# student.change_name("Andrew")
# student.change_name("Sabrina")
# student.change_name("Garrett")
# atlanta_student.change_name("Jason")


# class Phone(object):
    
#     def __init__(self, phone_type):
#         self.phone_type = phone_type
#         self.status = "off"
#         print(f"my phone is a {self.phone_type}")

#     def print_phone(self):
#         print(self.phone_type)

#     def on(self):
#         print('on')
#         self.status = "on"

#     def off(self):
#         print('off')
#         self.status = "off"
    
#     def get_status(self):
#         print(f'your {self.phone_type} phone is currently: {self.status}')


# android = Phone("android")
# iPhone = Phone("iPhone")
# blackberry = Phone("blackberry")

# android.get_status()
# android.on()
# android.get_status()

# iPhone.get_status()
# blackberry.get_status()



# import datetime # we will use this for date objects
# class Person:
#     def __init__(self, name, surname, birthdate, address, telephone, email):
#         self.name = name
#         self.surname = surname
#         self.birthdate = birthdate
#         self.address = address
#         self.telephone = telephone
#         self.email = email

#     def age(self):
#         today = datetime.date.today()

#         age = today.year - self.birthdate.year

#         if today < datetime.date(today.year, self.birthdate.month, 
#         self.birthdate.day):
#             age -= 1
#         return age

# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12), # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com"
# )

# print(person.name)
# print(person.email)
# print(person.age())


class Car: 
    pi = 0
   

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.doorStatus = "closed"
        print(f"make: {self.make} model:{self.model} color:{self.color}")
        self.myList = []
        Car.pi = 5

    def ChangeColor(self, newColor):
        self.color = newColor
        return (self.color)


    def openDoor(self):
        self.doorStatus = "open"

    def displayColor(self):
        print(f"The color of your {self.make} is {self.color}")

    def displayInfo(self):
        print(f"make: {self.make} model:{self.model} color:{self.color}")

    def cir(self, length):
        return 2 * Car.pi * length

    def override(self):
        print("override of car class")

    def altered(self):
        print("altered of car class")


class ElectricCar(Car):

    def __init__(self, electricMotor, make, model, color):
        self.electricMotor = electricMotor
        super(ElectricCar, self).__init__(make, model, color)

    def printCarType(self):
        print("I'm an electric car")
    

    def override(self):
        print("override of electric car class")

    def altered(self):
        print("BEFPRE altered of electric car class")
        super(ElectricCar, self).altered()
        print("After altered of electric car class")

    def motorType(self):
        print(self.electricMotor)



ec = ElectricCar("ac motor", "tesla", "s", "red")
ec.printCarType()
ec.ChangeColor("green")
ec.displayInfo()

ec.override()
ec.altered()
ec.motorType()

ec2 = ElectricCar("dc motor", "nissan", "leaf", "yellow")
ec2.printCarType()
ec2.ChangeColor("blue")
ec2.displayInfo()

ec2.override()
ec2.altered()
ec2.motorType()


# class HybridCar(Car):

#     def printCarType(self):
#         print("I'm a hybrid car")

# print(Car.pi)

# Car.greeting

# toyota = Car("toyota", "prius", "green")




# toyota.greeting

# honda = Car("honda", "civic", "purple")



# Car.pi =4

# print(honda.cir(2))

# print(toyota.pi)
# print(honda.pi)

# jeep = Car("jeep", "wrangler", "white")

# print(jeep.pi)

# f150 = Car("Ford", "f150", "marble")

# print(f150.cir(3))


# f150.ChangeColor("Midnight Red")
# f150.displayColor()

# toyota.displayInfo()
# honda.displayInfo()
# jeep.displayInfo()
# f150.displayInfo()

# fleet = [toyota, honda, jeep, f150]

# for carObject in fleet:
# #     print(carObject.displayInfo())


# class Person:
#   def __init__ (self, name):
#     self.name = name
#     self.count = 0
#     self._a = 1
#     self.__b = 5

#   def greet (self):
#     self._greet()

#   def _greet (self):
#     self.count += 1
#     if self.count > 1:
#       print("Stop being so nice")
#       self.__reset_count()
#     else:
#       print("Hello", self.name)
      
#   def __reset_count(self):
#     self.count = 0


# person = Person("Sabrina")

# person.greet()
# person.greet()
# person.greet()
# print(person._a)
# print(person._Person__b)


# class Animal:
#     def __init__ (self, name):
#         self.name = name
    
#     def fourleggs(self):
#         print("i have 4 legs")



# class Dog(Animal):
#     def woof(self):
#         print("Woof")

# puppy = Dog("pickle")
# print(puppy.name)
# puppy.woof()
# puppy.fourleggs()

# puppy2 = Dog("john luke")
# print(puppy2.name)
# puppy2.woof()
# puppy2.fourleggs()




# class Cat (Animal):
#   def meow (self):
#     print("Meow")

# cat1 = Cat("misty")
# cat2 = Cat("bubbles")

# print(cat1.name)
# cat1.meow()
# cat1.fourleggs()
# print(cat2.name)
# cat2.meow()
# cat2.fourleggs()







