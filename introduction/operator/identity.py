"""
is the identity operator in python. It is used to compare the memory location of two objects. It returns True if both objects are the same object, otherwise it returns False.
is not - returns True if both objects are not the same object, otherwise it returns False.
"""

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b) # True, because both a and b refer to the same object in memory
print(a is c) # False, because a and c refer to different objects in memory
print(a is not c) # True, because a and c refer to different objects in memory