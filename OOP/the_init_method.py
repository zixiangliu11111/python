#Python _init_() Method
"""

All classes have a built-in method called __init__().
which is always executed when the class is being initiated.

The _init_() method is used to assign values to object properties,
or to preform operations that are necessary when 
the object is being created,
"""

#E.g. create a class nameed Person, use the _init_() method
"""
class Person:    #Class
    def _init_(self, name, age):   #self, nameland and age are paramets
        
        self.name = name           #Property
        self.age = age             #property

person1 = Person("Alan Turing", 40)   #Object

#Output
print(person1.name)
print(person1.age)
"""
#E.g. Without the _unit_() method
"""
we would to set properties manually for each object

"""
class PersonClass:
    pass      #Pass statement  help to avoid getting an error.

p1 = PersonClass()
p1.name = "Mr. Spock"
p1.age = 80

print(p1.name)
print(p1.age)



#Default Value in __init__()
"""
We can also set default values for parameters in the __init__() method:
"""

#E.g.: Set a default value for the age parameter:

class Benfica:
    def __init__(player, name, position, tshirt, nationality):    #Funcion with parameters
        player.name = name                     #Property defined in string
        player.position = position             #Property defined in string
        player.tshirt = tshirt                 #Property defined in int
        player.nationality = nationality       #Property defined in string

player1 = Benfica("antonio","defense",4,"Portuguese")    #Objects 
player2 = Benfica("Tomas","defense",44,"Portugueses")    #Objects
player3 = Benfica("Otamendi","defense",30,"Argentinian") #Objects

#Output
print(player1.name,player1.position,player1.tshirt,player1.nationality)
print(player2.name,player2.position,player2.tshirt,player2.nationality)
print(player3.name,player3.position,player3.tshirt,player3.nationality)

