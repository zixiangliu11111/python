#Python if Statement
"""
Python Conditions and if statements
Python supports the usual logical conditions from mathematics

- Equals: a == b
- Not Equals: a |= b
- Less tahn: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b
"""

#Eg. if statement

a = int(input("a: "))
b = int(input("b: "))

if a<b:   #Statement and will return false or ture
    print("True")
else:
    print("False")

#Indentation(Bug in Python)
"""
If statement, without indentation(show us an error)
"""
#Eg.
"""
x = 22
y = 500
if x > y:
print("x is greater than y") #return an error
"""

#Using variables in contitons
login = True
if login:
    print("weicome fella")

