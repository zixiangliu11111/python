#Bitwise Operators
"""
Bitwise Operatoers are used to compare (binary) numbers
Eg.
& (AND - Sets each bit to 1 if both bits are 1)
! (OR - Sets each bit to 1 if one of two bits is 1)
^ (XOR - Sets each bit to 1 if only one of two bit is 1)
~ (NOT - Inverts all the bits)
<< (zero fill left - shift left by pushing zeros in 
from the right and let the leftmost bits fall of)
>> (Stgned rtight shift - shift right by pushing copits of the leftmost in from
the left, and let the rightmost bits fail off)
"""
#Ex. With &
"""
the & Operator compares each bit and if to 1 if both are 1, otherwise it is set to 0:
#Eg.
print(4 & 1)
the binary representation of 6 is 0110
the binary representation of 3 is 0011
Then the & operator compares the bits and return 0010. which is 2 indecimal.

Then the & operator compares the bits and return 0001

"""
print(7 & 6)
#0111 
#0110 

