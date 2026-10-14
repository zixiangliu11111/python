#Python Polymorphosm
"""
The word "polymorphism" means "many forms", and in programming it refers to
method/functions/operators with the same name that can be executted on 
many objects or classes
"""

#Function Polymorphism
"""
An examplo of a Python function that can be used on different objects is the 
len() functions.

for strings len() returns the number of characters:
"""
#Eg.
x = "Hello world"

print(len(x))

#For tuples len() return the number of items in the tuple:
myTuple = ("Zi", "Robalo", "Claudio")
print(len(myTuple))

#For dictionaries len() return the number of key/value paires in the dictionary:
thisdict = {
    "brand": "audi",
    "model": "R8",
    "year": 2018
}
print(len(thisdict))

#Class Polymorphism
"""
Polymorphism is often used in Class methods, Where we can have multiple classes 
with the same method name.

For examplo,say we have three classes:car, Boat, and Plane, and
they all have a method called move():
"""

#E.g.: Dfferent classes with the same method:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(slef):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")           #Create a Car object
boat1 = Boat("Ibiza", "Touring 20")     #Create a Boat object
plane1 = Plane("Boeing", "747")         #Create a Plane object

for x in(car1, boat1, plane1):
    x.move()

"""Look at the for loop at the end. Because of polymorphism 
we can esecute the same method for all three classes."""

#Inheritance Class Polymorphism
"""
What about classes with child classes with the same name?
Can we use poly

Yes, If we use the example above and make a parent class called Vehicle, and make
car, Boat, Plane child classes of Vehicle methods , but can override them:
"""

#E.g. Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicie:

class Vehicie:
    def __init__(self, brand,model ):      #This is a method with three parameter
        self.brand = brand                 #This is a property
        self.model = model                 #This is a property

    def move(self):              #This is a method
        print("move!")           #This is a output

class Car(Vehicie):              #this is a child class
    pass

class Boat(Vehicie):             #This is a child class   
    def move(self):              #This is a method with parameter
        print("Sail!")           #This is a output

class Plane(Vehicie):            #This is a child class
    def move(self):              #This is a method with parameter
        print("fly!")            #Output


car2 = Car("Ford", "Mustang")    #This is a object
boat2 = Boat("YAMAHA","JOKE")    #This is a object
plane2 = Plane("Boeing","828")   #This is a object


for list in(car2,boat2,plane2):
    print(list.brand,list.model)

    list.move


"""

Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand,

The Boat and Plane classes also inherit brand, model and move()
from Vehicle, but they bith override the move() method,

Recause of polymorphism we can execute the same methods for all classes.



"""

