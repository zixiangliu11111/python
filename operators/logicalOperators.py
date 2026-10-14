#Logical Operators
"""

Logical operators are used to combine conditional statements:
Eg.
and (Returns True if both statements are True)
or (Returns True if one of the statements is True)
not (Reverse the result, returns false if the result is true)


"""
#Ex. with and
x=2
print(x > 0 and x < 5)

#Ex. with or
print(x < 0 or x < 5) #Return True
print(x < 0 or x > 5) #Return False

#Ex. with not
print(not(x < 5)) #Return False
print(not(x > 5)) #Return True