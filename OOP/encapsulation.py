#Python Encapsulation

"""
Encapsulation is about protecting data inside a class

It means keeping data(properties) and methods together in a class, while controlling
how the data can be accessed from outside the class.
This prevents accidental changes toyour data and hides the internal details of
how your class works.
"""

#Private Properties

"""
In Python,you can make properties private by using a double underscore __ prefix:
"""
#E.g.: creating a private class property named __agr:
"""
class Person:
    def __init__(self,name, age):
        self.name = name
        self.__age = age    #This is Private property

p1 = Person("Gisela",19)
print(p1.name,)
print(p1.__age)       #This will return error, because the private property
"""
"""
Private properties cannot be accessed directly from outside the class 
"""


#E.g.: Geting Private Property ValueError
"""
To access a private property, we can create a getter method:
"""

class Student:
    def __init__(self, studentName, studentAge):
        self.Name = studentName
        self.__age = studentAge
    def get_age(self):
        return self.__age


student1 = Student("Tomas",17)
print(student1.Name)
print(student1.get_age())


#Set Private Property Value
"""
To modify a private property, we can create a setter method.
Rhe setter method can also validate the value brfore setting it:
"""

#E.g. using a setter methed to cahnge a private property.

class custumer:
    def __init__(self, fisrtName, lastName,age):
        self.name = fisrtName
        self.__surname = lastName
        self.__age = age

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age > 18:
            self.__age = age
        else:
            print("You need to waint until 18!")


custumer1 = custumer("James","Maxwell",20)
print(custumer1.get_surname())

custumer1.set_age(17)
print(custumer1.get_age())

"""
Why Use Encapsolulation? 

Encapsolation provides serveral banefits:
- Data Protection: Prevents accidental modification of data
- Validation: We can validate date before setting it
- Flexibility: Internatinal implemetation can change without affecting externl code
- Control: We have full control over how data is accessed and modified

"""

#E.g. Using encapsulation to protect and validate data.

class Student:
    def __init__(self, name):
        self.studentName = name
        self.__grade = 0

    def set_grade(self, grade):                   #This method request a new infermation and check the data with a centition True or False
        if 0 <= grade <= 100: 
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):     #This method we are going read the privite information 
        return self.__grade

    def get_situation(self):          
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

Student2 = Student("Lucas")
Student2.set_grade(16)
print(Student2.get_grade())
print(Student2.get_situation())


#Protected Properties

"""
Python also has a convertion for protected properties using a single underscore _ prefix:

E.g. creating a protected property:
"""

class Employee:
    def __init__(self, name, Salary):
        self.name = name
        self.Salary = Salary 

employee1 = Employee("Gisela", 10000)
print(employee1.name, employee1.Salary)    #Wecan access, but we shouldn't



#Private Methods
"""
Create a private method:
"""

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, number):
        if not isinstance(number, (init,float)):
            return False
        return True

    def add(self, number):
        if self.__validate(number):
            self.result += number
        
        else:
            print("Invalid number")

clac = Calculator()
clac.add(5)
clac.add(12)

print(clac.result())


