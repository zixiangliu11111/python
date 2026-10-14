#Python Elif Statement
"""
The Elif keywor

The elif keywork is Python way of saying
"if the previus conditions were not true.

The elif keywork allows you to check multiple expressions for True.
"""

#Eg.
age = 18
student = 16
if student > age:
    print("You are allowed to drink alcohol")
elif age > student:
    print("Sorry,You stil to young to drink alcohol")

#Eg.with multiple Elif statements

score = int(input("score: "))

if score >= 19:
    print("Fair play to you! Well done!")
elif score >= 17:
    print("Well done")
elif score >= 14:
    print("Good job")
elif score >= 10:
    print("Don't give up")
elif score <= 9:
    print("Sorry, You must to do athoner exam")

#Eg. categorizing age groups

age = int(inpt(":"))

if age <13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("you are a senior")
