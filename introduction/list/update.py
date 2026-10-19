lst = [1, 2, 3, 4, 5]
print(f'before list{lst}')
lst[0]= "hello"
print(f'after list{lst}')
lst[0:3] = [10, 20, 30]
print(lst)