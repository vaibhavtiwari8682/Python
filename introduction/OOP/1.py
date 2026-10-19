class Student:
    def __init__(self,name,age,grade):
        self.name =  name
        self.age = age
        self.grade = grade

        #creating objects
student1 = Student('Rakesh', 100,'A+')
student2 = Student('ramesh', 50,'A')

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)

"""
Types of constructor
1. default constructor - constructor having no parameter only self is passes
2. Parameterised constructor - parameters are passed like name , age , self
3. constructor with default values - : A constructor with default values provides automatic values when no values are given while creating an object.

"""