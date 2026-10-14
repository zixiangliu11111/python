#Variables names:(Nome de variavels)
"""
Variables are memory Box use to sava an information
A variable can have a short name(eg. x ou y) or a more descriptive name(eg, age, carname,total)

Rutes for python variables(Regres para variavel em python)
- A variable name must sstart with a letter or underscore character eg. maria ou _maria
- A variaables name cannet start with a nuber eg. 123maria - #error
- A variable name cannet be any of the python keywords eg. print..
"""
#Examplo of legal variables names:
# mycar = "Tesia"
# my_car = "Tesia"
# _my_car = "Tesia"
# mycar ="Tesia" #Type Cameicase
# MYCAR ="Tesia"
# mycar007 ="Tesia"

#Examplo o illegal names:
#3mhvar = "Maria"
#my-var = "Maria"
#my var = "Maria"

#Many values to multiple variables
"""
python alloiwsa you to assign values to multiple varibles in one line:
"""
"""
Examplo
x, y, z = "粑粑", "粑粑王","粑粑大王"
print(x)
print(y)
print(z)
"""
#One value to multiple varibles
"""
And you can assigin the same value to multiple varibles in one line.
"""
#Example
# x = y = z ="粑粑"
# print(x)
# print(y)
# print(z)


#Unpack a collection
"""
if you have collecton of values in a list, typle etc..
Python aloes you to extract the volues into variables
This is cailled unpacking.

Se vocé tiver uma coleção de valores em uma lista, tupla etc.
 python permite extrair os valores em variaveis. Isso é chamado de descompactação
"""
#Exemplo
"""Unpack a list;"""
"""fruits = ["apple","banana","cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)
"""
#Global Variables
"""
Variables that are created outside of a fuction(as in all of the examples in the previus page)
are know as global variables.

Global variables can be used by everyone, both inside of fuctions and outside
"""
#Examplo
#Creato a variable outside of fuction, and use it inside the fuction
"""
x="Agent Gisela" #outside of fuction

def agenName(): #Keyword "def" to create a fuction in python
    print("python is" + x)

agenName()

#Examplo when we create a variable inside a fuction
x="Agent 留"
def agentName():
    x="Agent Valentin"
    print("Python is" + x) #Called a variable inside a fuction => Agent Valetin

agentName()
print("Python is" + x) #Called a variable outside a fuction => Agent 留
"""

#Global Varable
"""
Variable that are created outside of a fuction are know as global variables.
Global varable can be used by everyone, both inside of fuction and outside.
"""
#Exemplo
"""
def myFuction():
    global name
    name = "Daniel"

myFuction()
print("Agent is " + name)
"""

#exerciocios
"""
lalala = "Gisela"
def gisela():
    lalala = "Daniel"
gisela()
print("Agent is " + lalala)
"""

"""
def gisela():
    global name
    name = "Gisela"
gisela()
print("Agent is " + name)
"""

numero = int(input("numero "))

if numero > 0 and numero < 9 :
    print("True")
else:
    print("False")
    
