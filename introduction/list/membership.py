'''
in - true /false
not in - oppsosite of in
'''

lst_1 = [1, 2, 3, 4, 5]
check = int(input("enter a number to check in list = "))
if check in lst_1:
    print("found")
else:
    print("not found")