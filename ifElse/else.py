#Python Else Statement

"""
The else keywork catches anything wich isn't caught by preceding condition.(False)

"""

#Eg. with Else

x = 20
y = 15

if x > y:
    print("x is greater than y")
elif x == y:
    print("ax and y are equal")
else:
    print("x is less than y")


#Eg with Else without Elif
age = 18 
student = 16

if student <= age:
    print("You can not see this film!")
else:
    print("You can see this film!")