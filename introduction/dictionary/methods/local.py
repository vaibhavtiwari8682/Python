#A local variable is a variable that is created inside a function and can normally be used only inside that function.
def msg():
    choice = "i love myself"
    print(choice)

    msg()
    print(choice)