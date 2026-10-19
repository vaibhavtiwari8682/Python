num_1 = float(input("enter number 1 = "))
num_2 = float(input("enter number 2 = "))

choice = input("enter your choice + - * /  //  % = ")

if choice == '+':
    print(num_1 + num_2)

elif choice == '-':
    print(num_1 - num_2)

elif choice == '*':
    print(num_1 * num_2)

elif choice == '/':
    print(num_1 / num_2)    

elif choice == '//':
    print(num_1 // num_2)

elif choice == '%':
    print(num_1 % num_2)

else :
    print('invalid choice')
                