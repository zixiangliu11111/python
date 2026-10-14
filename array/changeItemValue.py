#Python - Change List items
"""
To change the value of a specifc item, refer to the index number:
"""

#Eg.
prefix = ["quetta","ronna","yotta","zetta",]
prefix[1] = "quecto"
print(prefix)
aluno = ["valtin","martim","Luca","thomas","tomas","Zi","Nitton","Gonçalo","miguel","dinis"]
aluno[3:5] = ["2", "1"]
print(aluno)

#Change a Range of Item Values
"""
To change the value of items within a spacific range
"""
#Eg.  change the values "banana" and "cherry" with the values "blakcurrant" and "watermelon"
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1:3] = ["black", "watermelon",]
print(fruits)

#Insert Items
"""
The insert() method inserts an item at the specified index .
"""

#Eg. Insert "Deniel" as the third item:
student = ["Robalo", "Climon", "Martim"]
student.insert(2, "Daniel")
student.insert(3, "")
print(student)