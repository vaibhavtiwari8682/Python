# yield keyword used for generator
#A generator is a special type of function that produces values one at a time, instead of producing all values at once.
def count_down(num):
    while num > 0:
       yield num #yield values one at a time
       num -= 1
    #using the generator
for number in count_down(5):
    print(number)

    #decorator and generator differencxe in one line
#Decorator adds/changes the behavior of a function, while a Generator produces values one at a time using yield