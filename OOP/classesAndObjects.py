#Python Classes and Objects
"""
Alomst everything in python is an objects with its properties and method.
"""

#Create a class

"""
To create a class, we use the keyword class
"""

#Eg. create a class nammed MyClass,with a property named x:
class Myclass: #Creating class
    x = 15    #property

print(Myclass)   #Call class

#E.g. create object
"""
Now we can use the class named MyClassBody to create objects

Create an object named part1, and print the value of HEAD.
"""

class MyclassBody: #Creating class
    head = 1    #property

part1 = MyclassBody   #created an object
print(part1.head)   #Called the object and the property of object


#creating a student class


class studentClass:
    name = "Zi"
    id = 24
    coruse = "PTEI"
    kit = True
idStudent = studentClass()
coursestudent = studentClass()
KitDigital = studentClass()

print(studentClass.name)
print(idStudent.id)
print(coursestudent.coruse)
print(KitDigital.kit)

