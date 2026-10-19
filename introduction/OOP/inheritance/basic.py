class Animal:
    def speak(self):
        print('Animals make sounds')

class Dog(Animal):
    def bark(self):
        print('dogs bark')

dog = Dog()
dog.speak()
dog.bark()                