#Identity Operators
"""
Identity operators are used to cpmpare th objects, not if they
but if they are actuaily same object, with the same memory
location:
Eg.
is (Return True if both variables are the same object)
is not (Return True if both variables are not the same object)
"""
#Ex.
x = ["Apple", "Banana"]
y = ["Apple", "Banana"]
z = x

print(x is z) #Return True
print(x is y) #Return False
print(z is y) #Return False
print(x == y) #Return True

#Ex. with is not
print(x is not y) #Return True

#what is the difference between is and ==?
"""
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""
#Ex.
d = [1,2,3]
e = [1,2,3]
f = d
print(d == e)
print(d is e)
