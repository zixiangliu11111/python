#Python Membership Operators
"""
Membership Operators are used to test if a sequence is presented in an object:
Eg.
in (Return True a sequence with the specified value is present inthe object)
not in (Return Ture if a sequence with the spacified value is not present in the object)
"""
#Ex. check if "Banana" is present in list:
fruits = ("Apple", "Banana", "Cherry" )
print("Apple" in fruits)
print("Banana" in fruits)
print("Cherry" in fruits)

"""
the menbership operators alse work with string
"""

#Ex.
text = "hello word"
print("hello" in text)
print("H" in text)
print("h" not in text)
print("b" not in text)
print("hello word" in text)
print("helloword" in text)

