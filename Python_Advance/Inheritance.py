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
class Grandfather:
    def grandfather_method(self):
        print("Grandfather class method")
    def show(self):
        print("Grandfather show method")
class Father(Grandfather):
    def father_method(self):
        print("Father class method")
    def show(self):
        print("Father show method")
class Child(Father):
    def child_method(self):
        print("Child class method") 
obj=Child()
obj.grandfather_method()  #Grandfather class method
obj.father_method()       #Father class method      
obj.child_method()        #Child class method

obj.show()                #Father show method