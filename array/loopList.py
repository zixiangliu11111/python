#python loop List - Python

#Loop through a list
"""
We can loop throught the list items by using a "for" loop 
"""

#Eg.with "for"
ptei = ["Robalo", "Santiago", "Gabriel", "Thomas", "Daniel", "Nilton"]

for x in ptei:
    print(x)

#Loop Through the Index Numbers 
"""
Use the range() and len() fuctions to create a suitable iterable.
"""

#Eg:

for y in range(len(ptei)):
    print(y, ptei[y])

