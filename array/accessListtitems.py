#Python - Access List Items
"""
List items are indexed and you can access
them by referring to the index number:
"""
#Eg. print the seccond item of the list:
school = ["Classsroom", "Desk", "Cupboard", "Shelf"]
print(school[1])

#Negative Indexing
"""
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.
"""
#Eg.print the last item of the list:

units = ["second", "metre", "kilogram", "ampare", "kelvin", "mole", "candela"]
print(units[-1])

#Range of Indexes
"""
You can specify a range of indexes by specifying where to start and where to end range
"""
print(units[2:5])

print(units[0:4]) #Returns the items from beginning to ampare
print(units[2:]) #Returns the items from kilogram to the end candela
