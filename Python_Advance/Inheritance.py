# class Parent:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):  #function definition
#         print("greet from parent")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  #inheritance
#         self.age = age
#     def greet(self):  #function overriding
#         print("greet from child")

# obj1=Child("John", 12)
# obj2=Parent("Doe")

# obj1.greet()
# obj2.greet()

# print(obj1.name, obj1.age)
# print(obj2.name)



# multiple inheritance example
# class Father:
#     def show(self):
#         print("Father class method")
# class Mother:
#     def display(self):
#         print("Mother class method")
# class Child(Father, Mother):
#     def info(self):
#         print("Child class method")


# obj=Child()
# obj.show()     #Father class method
# obj.display()  #Mother class method
# obj.info()     #Child class method



# multilevel inheritance example
# class Grandfather:
#     def grandfather_method(self):
#         print("Grandfather class method")
#     def show(self):
#         print("Grandfather show method")
# class Father(Grandfather):
#     def father_method(self):
#         print("Father class method")
#     def show(self):
#         print("Father show method")
# class Child(Father):
#     def child_method(self):
#         print("Child class method") 
# obj=Child()
# obj.grandfather_method()  #Grandfather class method
# obj.father_method()       #Father class method      
# obj.child_method()        #Child class method

# obj.show()                #Father show method


# Polymorphism example
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
 
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# def animal_sound(animal):
#     animal.sound()
# dog=Dog()
# cat=Cat()   
# animal_sound(dog)  #Dog barks
# animal_sound(cat)  #Cat meows



# Encapsulation example
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  #private attribute
#     def status(self):
#         if self.__balance >= 0:
#             print("Account is in good standing.",self.__balance)
#         else:
#             print("Account is overdrawn.")

# obj = BankAccount(100)
# obj.status()  #Account is in good standing.


# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# rect = Rectangle(5, 10)
# print("Area of rectangle:", rect.area())  #Area of rectangle: 50


