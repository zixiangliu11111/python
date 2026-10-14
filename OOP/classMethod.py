#Python Class Methods
"""

Methods are functions that pelong to a class. They define the
behavior of objects created from the class.
"""

#Eg. with Math

class calculator:              #This is a class
    def add(self, x, y,):      #This is a method with parameter
        return x + y
    def multiply(self, x, y):
        return x * y


clac = calculator()            #This an object

print(clac.add(2,3))
print(clac.add(2,-6))

print(clac.multiply(2,2))
print(clac.multiply(3,-4))

#Method Acceessing Properties
"""
Method can access and modify object properties using self:
"""

#E.g a method that accesses object properties

class Custumer:                        #This is a class 
    def __init__(self, name, address): #This is a method w/ parameters
        self.name = name               #This is a property         
        self.address = address         #This is a property

    def get_info(self):                #This is a method with a parameter
        return f"{self.name} is living in {self.address} city"  #Return a mesage with properties
    
custumer1 = Custumer("Toy", "Viana de Castelo")

print(custumer1.get_info())



#Method Modifying Properties
"""
Method can modify the properties of an object  
"""

class supplier:
    def __init__(self, conpanyName, product):
        self.conpanyName = conpanyName
        self.product = product

    def stockAvailable (self):
        self.product += 1
        print(f"New product in stock: it is {self.product} units available!")


product1 = supplier("Sansung", 19)

#Output
product1.stockAvailable()
product1.stockAvailable()




#The __str__()Method
"""
class Decathlon:
    def __init_(self, decathlonSection, decathlonProduct):
        
        self.decathlonSection = decathlonSection
        self.decathlonProduct = decathlonProduct

decathlon_now = Decathlon("Futboll", "Adidas")
print(decathlon_now)  #Return an error
"""
#E.g. with the __str__() method:

class sportZone:
    def __init__(self, sportZoneSection, sportZoneProduct):
        self.sportZoneSection = sportZoneSection
        self.sportZoneProduct = sportZoneProduct
    def __str__(self):
        return f"{self.sportZoneSection} : ({self.sportZoneProduct})"

sportZone_new = sportZone("Basketball", "Nike")
print(sportZone_new)

#Multiple Methods
"""
A class can have multiple methods that work toogether
"""

#E.g Create multiple methods in class:

class playlist:                         #This is a class
    def __init__(self,name):            #This is a method with parameters
        self.name = name                #This is a property
        self.songs = []                 #This is a property

    def add_song(self, song):          #This is a method w/ parameters
        self.songs.append(song)        #THis property with append() method is used add an element to the end of a list
        print(f"Added. {song}")        #Output with string

    def trmove_song(self, song):       #This is a method with parameters
        if song in self.songs:         #Condition if... in
            self.songs.remove(song)    #This is property with remove() method
            print(f"Removed: {song}")  #Output 

    def show_songs(self):              #This is a method
        prtin(f"Playlist '{self.name}':") #Output
        for song in self.songs:        #This is a loop in python
            print(f"-{song}")          #This is output inidide the loop


my_playlist = playlist("Favorites")    #calling the class()
my_playlist.add_song("Fernando Daniel") # calling the method add.song()
my_playlist.add_song("Caroling Deslandes")  #Calling the methid add,song()
my_playlist.add_songs() #Calling the method show_songs

#Delete Methods
"""
You can delete methods from a class using the del keyword:
"""

#E.g. Delete a method from a class:

class Game:
    def __init__(self, player):
        self.player = player

    def greet(self):
        print("Hello Nub")

player1 = Game("Carlos")

del Gama.greet

player1.greet() #This will cause an error """"""""""""""""2222222"

