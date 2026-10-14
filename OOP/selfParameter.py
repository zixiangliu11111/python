#Self Parameter
"""
The self paramere is a reference to the current instance 
of the class.
It is used to access properties and methods 
that belong the class.
"""
#Eg. we can use self to access class properties 
class Student:        
    def __init__(self, name, age):   #This is a fuction or method with prarameter
        self.name = name             #This a property, an association with the name parameter
        self.age = age               #This a property, an association with the age parameter

    def greet(self):   #This is a new fuction to return a message
        print("Welcome, new student ", self.name,self.age)  #Print method or parameter

student1 = Student("Daniel", 16)    #This is an object with values
student2 = Student("David", 18)     #This is an object with values

student1.greet()    #This is an object calling greet method
student2.greet()    #This is an object calling greet method

#Watchout the self parameter must be the firsat parameter of any method in the class
"""
Without self, Python would not know wiich object's properties we want to access 
18
"""
