
# class MyClass:
#     def SayHello():
#         print("Hello there!")
#     def greeting(self):
#         print('Hello')


# person = MyClass()
# person.greeting()
# person.SayHello()
# MyClass.SayHello()

# class MyClass:
#     Greeting = ""
#     def SayHello(self):
#             print("Hello {0}".format(self.Greeting))
#     def SetGreeting(greetingName):
#         MyClass.Greeting = greetingName
#     def setMyCopy(self, greeting):
#         self.Greeting = greeting

# MyClass.Greeting = "Zelda"
# MyClass.SetGreeting("Veronica")
# # MyClass.SayHello()
# test = MyClass()
# test.SayHello()
# test.setMyCopy("Lino")
# test.SayHello()
# test2 = MyClass()
# test.SayHello()

# class Person:
#   GlobalPerson = "Zelda"
  
#   def __init__ (self, name):
#     self.name = name
#     self.me = ''
#   def greet (self, friend):
#     self.me = friend
#     print("Hello {} and {} and {} and {}".format(self.name, friend, self.GlobalPerson, self.me))

# me = Person('Paul')
# me.greet('Pepper')

# matt = Person('Matt')
# matt.greet('Eric')

# travis = Person('Travis')
# travis.greet('Hussein')

# Person.GlobalPerson = "Skylar"
# me.greet('Pepper')
# matt.greet('Eric')
# travis.greet('Hussein')


# class Person:
#   def __init__ (self, name):
#     self.name = name
#     self.count = 0
#   def greet (self):
#     self.__greet()
#   def __greet (self):
#     self.count += 1
#     if self.count > 1:
#       print(self.count)
#       print("Stop being so nice")
#       self.__reset_count()
#     else:
#       print(self.count)
#       print("Hello", self.name)
#   def __reset_count(self):
#     self.count = 0

# person = Person("Veronica")
# person.greet()
# person.greet()
# person.greet()


class Test(object):
    def __init__(self):
        self.__a = 'a'
        self._b = 'b'

t = Test()
print(t._b)
print(t._Test__a)