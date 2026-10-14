"""
Inheritance allows us to define a class that inherits all 
the methods properties from another class.

parent class is the class being inherited from, also called base class.

child class is the class that inherits from another class, also called derived class.

"""

#Create a parent Class
"""E.g. Create a class named Person, with firstname and lastname properties, and a print,
and a printname method"""

class Person:
    def __init__(self, ftname, lname): #This is a method with parameters
        self.firstname = ftname       #This is a property
        self.lastname = lname          #This is a property
    
    def printName(self):
        print(self.firstname, self.lastname)

#We use the Person class to create an object

user1 = Person("Alan", "Turing")

user1.printName()


#Create a Child Class
"""
To create a class that inherits the functionality from another class, send the parent
class as a parametor when creating the child class.
""" 

#E.g. Create a class named student

class Student(Person):
    pass

user2 = Student("Marie", "Curie")
user2.printName



