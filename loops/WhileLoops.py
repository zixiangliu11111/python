#Python while Loops 
"""
Python has two primitive loop commands
- while loops
- for loops
"""

#The while loops
"""
The while loop can execute a set of statements as long a contion is true 
"""

#Eg.print delta as long as delra is less than 6
"""
delta = 1

while delta <= 6:
    print(delta)
    delta += 1
"""

#The break Statement

"""
With the break statement we can stop 
the loop even if the while condition is true:
"""

#Eg. Exit the loop when beta is 3:
beta = 1
while beta < 6:
    print(beta)
    if beta == 3:
        break
    beta += 1 #add 1 to beta

"""
and continue with the next:
"""

#Eg. continue to the next iteration if 1 is 3:

i = 0             #i is a variable
while i <6:       #condition return true or false
    i += 1        #add 1to i variable
    if i == 3:    #our second condition
        continue  #continuous processing the code
    print(i)

#The else Statement

"""
With the else statement we can run a block of code once when 
the condition no longer is true
"""

#Eg.Print a message once the condition is false:
alpha = 1
while alpha < 0:         #checking if the condition is true
    print(alpha)
    alpha += 1
else:    #output when variable is false
    print("i is no longer less than 6")  #output when the condition is false

