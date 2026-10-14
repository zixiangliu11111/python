#Python class properties

"""
Properties are variables that belong to a class. 
They store data for each object created from the class.
"""

#E.g.creating a class with properties

class Person:                        #This is a class
    def __init__(self, name, age):   #This is a method with parameter
        self.name = name             #This is properties
        self.age = age               #This is properties

person1 = Person("Gonçalo ",25)      #This is an object
person2 = Person("Miguel", 18)       #This is an object

#output
print(person1.name, person1.age)
print(person2.name, person2.age)

#E.g. access properties
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

a = Car("Lamborghini","Huracan sterrato" )

print(a.brand, a.model)

#E.g. Modify Properties

class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

friend1 = Friend("Tobi", 40)
print(friend1.age)           #Original age

friend1.age = 4              #change age
print(friend1.age)


#Eg.Delete Properties

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = student("Dinis", 10)

del student1.age

print(student1.name)
#print(student1.age) #return an error



#E.g. class Properties vs object Properties

"""
Properties defined inside __init__() belong to each object(instance properties)
Properties defined output methods belong to the class itselft(class properties)
and are shared by all objects:
"""

class Animal:
    species = "Human"  #Class property

    def __init__(self, name):
        self.name = name #Instance property

person1 = Animal("Tobi")    #This is an object
person2 = Animal("Manuel")

print(person1.name, person2.name)
print(person1.species, person2.species)


#Modifying Class Properties
"""
When we modify a class property, it affects all objects
"""

#E.g.changing a class property 
class werehouse:
    productName = ""

    def __init__(self, brand):
        self.brand = brand

product1 = werehouse("Computer")
product2 = werehouse("Smartphone")

werehouse.productName = "Electronic"

print(product1.productName)
print(product2.productName)


#Add new properties

class Smartphone:
    def __init__(self, brand):
        self.brand = brand

phone1 = Smartphone("Apple")

phone1.model = 13
phone1.memory = 200

print(phone1.brand, phone1.model, phone1.memory)


