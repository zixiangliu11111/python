#Python For Loops
"""
A for loop in Python is used iterate over the items of any sequece
(such as a list, tuple dictionary, set, or string).
The loop executes a blovk of code once for each item in the sequece.
"""
#Example with cars

car = ["mercedez", "audi","jaguar"]
for cars in car:
    print(cars)


#The break Statement
"""
the brak statement allow stop the loop
"""

#Eg.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    #return apple and banana
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    #return apple and banana
    if x == "banana":
        break
    print(x)  #output after break return only apple