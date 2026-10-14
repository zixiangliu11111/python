#Data Type in Python
"""
Variables can ster data of different types and diffent types can do different things.

Text type: art
Numeric type: int, float, complex
sequence type: list, tuple,range
Mapping type: dict
Set type: set, flozenset 
Boolean type: bool
Binary type: bytes, bytearry, memoryview
None type: NoneType
"""

#Getting the type
"""
you can get the data type of any object by using the type() function:
"""
#Ex. String
school = "Miguel Torga College"
print(type("School"))

#Ex. Integer
age = 18
print("I am " + str(age)  + " The variable type is"+str(type(age)))

#Ex. float
ampere = 11.5
print(type(ampere))

#Ex. Complex coloiurs
colours = 1j
print(colours) #display colours
print(type(colours)) #display the data type of colours

#Ex.list
car = ["Citroen", "Peugeot","Alfa Romeo","Pagani"]
print(car) #display car
print(type(car))

#Ex. tuple
carTuple = ("Citroen", "Peugeot","Alfa Romeo","Pagani")
print(carTuple) #display carTuple
print(type(carTuple)) #display the data type of CarTuple

#Range(a set of similar things)
checkList = range(10)
print(checkList) #display checkList
print(list(checkList)) #convert to list to display the content of checkList

#Ex. dict
carDict = {"Name": "citroen", "year": "2025"}
print(carDict) #display carDict
print(type(carDict)) #display the data of carDict

#Ex. set
furniture = {"sofa", "chair", "Dinning table"}
print(furniture) #display furniture
print(type(furniture)) #display the data type of furniture

#Ex. frozenset
home = frozenset({"guess room", "hall", "Living room"})
print(home) #display home
print(type(home)) #display the data of home

#Ex. Bool
key = True
print(key) #display key
print(type(key)) #display the data type of key

#Ex. bytes
byteData = "Portugal"
print(byteData) #display byteData
print(type(byteData)) #display the data type of byteData

#Ex. with Bytearray data
bytearrayData = bytearray(10)
print(bytearrayData) #display bytearrayData
print(type(bytearrayData)) #display the data type of bytearrayData

#eX. with memoryview data
xy = memoryview(bytes(5))
print(xy) #display xy:
#display the data type of xy:
print(type(xy))

#Ex. with None
xz = None #display xz:
print(xz) #display the data type of xz:
print(type(xz))

#Ex. with python Numbers       #w/ = with
"""
There are three numeric types in Python:
-Int
-float
-Complex
"""

#Examples(E.g.)
x = 1 #Int
y = 2.8 #Float
z = 1j #complex

#verify the type with type() fuction:
print(type(x))
print(type(y))
print(type(z))
#Int data
"""
Int, or integer, is whole number, positive or negative,
without decimals, of unlimited lenght.
"""
#Examplo. with integers:
houseNumber = 2
apartmentNumber = 2345
weatherCelsius = -3

print(type(houseNumber))
print(type(apartmentNumber))
print(type(weatherCelsius))

#Float
"""
Float, oir "floating point number" is a number,
positive or negative, containing one or more decimals.
"""
#Eg. with floats:
adultHeight = 1.7
adultWeight = 50.5
bankAccount = -150.7
print(type(adultHeight))
print(type(adultWeight))
print(type(bankAccount))

#Eg.
"""
Complex numberd are written with a "j" as the imaginary part:
"""

#Eg. w/ complex:                                 w/ = with 
a = 1j + 4j
b = 5j
c = -5j

print(type(a))
print(type(b))
print(type(c))

#type comversion
"""
you can convert from one type to another with the int(); floaty(), and complex methods.
"""

#Eg.
e = 1 #int
f = 2.8 #float
g = 1j #complex

#convert from to float:
newE = float(e)

#covert from float to int
newF = int(f)

#convert from int to cpmplex
newConvertComplex = complex(g)

print(type(newE))
print(type(newF))
print(type(newConvertComplex))

#Random Numbers
"""
Python does not have a random() function to make a random number,
but Python has a built-in miduloe called random that can be uded to make random numbers:
"""

#Eg. impert the random module, and display a random number from 1 to 9
import random
print(random.randrange(1,101))


#python casting
"""
there may betimes when you want to sprcify a type on to a varlable.
 this can be done with casting.
Casting in py is therefore done using con structor functions:
- Int() - constructs an integer number
- Float() - constructs a float number 
- str() - constructs a string
"""
#Eg. w/ Integers:
house = int(1)
bbc = int(2.5)
country = int("351")
print(house)
print(bbc)
print(type(country))

#Eg. with floats:
rtp = float(1)
print(type(rtp))

#Eg. string:
age = str(16)
print(type(age))