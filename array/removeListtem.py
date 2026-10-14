#Python - Remove List Items

#Remove Specified Item
"""
The remove( method removes the specified item.
"""

#Eg. Remove "Messi"
fpf = ["Diogo costa", "Messi", "Gonçalo inacio", "Renato veiga", "Ruben dias", "joao palhinha", "Joao neves", "Bruno fernandes", "João cancelo", "João felix", "Ranfael leao", "Trincão"]

#Check how many objects a list contains. len() method
count = len(fpf)
print(count)

fpf.remove("Messi")
print(fpf)


#Remove specified Index
"""
The pop() method removes the is specified index
"""
fpf.pop(0)
print(fpf)

#del keyworld

del fpf[3]
print(fpf)

#Clear() method emties the list
fpf.clear()
print(fpf)


#Other methods

