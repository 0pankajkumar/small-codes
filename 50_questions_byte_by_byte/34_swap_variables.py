'''
Question​ : Given two integers, write a function that swaps them without using any
temporary variables
'''

a = 5
b = 10

print("Before swaping, a =",a ,"b=",b)

a = a*b
b = int(a/b)
a = int(a/b)

print("After swaping, a =",a ,"b=",b)