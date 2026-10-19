start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))

skip = int(input("Enter the  value u want to skip: "))

for i in range(start, stop):
    if i == skip:
        continue
    print(i)