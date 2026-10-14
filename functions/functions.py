#Python function
"""
A function is a block of code which only runs it is called.
A function can return data as aresult.
A function helps avoiding code repetition
"""

#Creating a Function
"""
A function is defined using the def keywork
"""
#Eg.
def my_function():            #Create a function
    print("Hello world")      #function tribute
    
my_function() #Calling function
my_function()
my_function()
my_function()


#Function Names
"""
- A function name must start with a letter or underscores 
- A function name can only contain letters, numbers, and underscores
- A function names are case-sensitive(myFunction and myfunction are different)

"""

#Eg.
"""calculate_sum()
_private_function
myFunction2()"""



#Eg. multiple a number
def calculate_mult(valorA):
    newValorA = valorA * 2

print(calculate_mult(2))

#Eg. sum a number
def calculate_sun(Valor):
    return Valor + 2

result = calculate_sun(2)

print(result)
print(calculate_sun(5))

#Return values
"""
Functions can send data back to the code that called them using the return statement
"""

#Eg.
def get_greeting():
    return "Hello Luca"

message = get_greeting()
print(message)



#The pass Statement
"""
Function defenitions cannot be empty. If you need to create a function
placehoider without any code, use the pass statement:

"""

#Eg.
def my_function():
    pass