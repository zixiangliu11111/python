#Python Inheritance
"""
Inheritance allows us 
to defing a class that inheritsall the method and properties from another class.

Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""


#Create a Parent Class
"""
Any class can be a parent class,so the syntaxis the same as creating any other class:
"""

#E.g.
"""
creating a class named Person, with firstname and Iastname,
and a printname method.
"""
"""
class Person:
    def __init__(Self, FName, IName):
        self.firstName = FName           
        self.IastName = IName   

    def printName(self):
        print(self.firstName, self.IastName)


x = Person("Albert", "Einstein")
x.printName()
"""

#Creating a Child Class
"""
To create a class that inherits the fucionality from another class, send the
parent class as a parameter when creating the child class.
"""
"""
#E.g.
class Student(Person):
    pass #Use the pass keywork when we do not want to add any other properties or methods to the class

y = Student("Isaac", "Newton")
y,printName()


class Father:
    def __init__(Self, eyesColour,hairColour, height):
        self.eyesColour=eyesColour
        self.hairColour=hairColour
        self.height=height
    def printFatherDNA(self):
        print(self.eyesColour,self.hairColour, self.height)

class child(Father):
    def __init__(self, eyesColour, hairColour, height):
        Father.__init__(self, eyesColour, hairColour, height)

x=child("Blue", "Black",190)
x.printFatherDNA()
"""

#Use the super() Function
"""
Python also has a super() function that will make the child
class inherit all the methods and properties from its parent.
"""

#E.g.

class indentification:
    def __init__(self, name, yearOfBirth):
        self.fname = name
        self.age = yearOfBirth

    def outputname(self):
        print(self.fname, self.age)
        self.graduationyear = 2024     #Add Properties, called graduationyear

class Employee(indentification):
    def __Init__(self,name,yearOfBirth):
        super().__init__(name,yearOfBirth)



    def welcome(self):
        print("welcome", self.fname ,"to Miguel torga Company","You were graduate in ", self.graduationyear)
        

new = Employee("Valentim", 2008)
new.outputname()
print(new.graduationyear)        #Output of new property from Employyer class 
new.welcome


"""
By using the super() function, we do not have to use the name of the parent, 
it will automatically inherit the methods and properties from parent.
"""

#E.g.

class Id:
    def __init__(self, name, mobilephone):  #This is a method with parameters
        self.fname = name                   #This is a property
        self.phone = mobilephone            #This is a property

    def readName(self):                    #New method call readname
        print(self.fname, self.phone)      #output of properties

class staff(Id):           #Second new class or child class  
    def __Init__(self,name,mobilePhone,year):
        super().__init__(name,mobilePhone)
        self.graduationYear = year     #Add Properties, called graduationyear

    def message(self):
        print("You can go home", self.fname)

new = staff("Santiago",94455588, 2027)
print(new.graduationYear)
new.readName()
new.message()
