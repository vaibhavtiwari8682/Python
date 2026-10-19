class Bird():
    def sound(self):
        print('Bird makes sounds')

class Crow(Bird):
    def sound(self):
        print('Crow say "Caw Caw"')

class Parrot(Bird):
    def sound(self):
        print('parrot sounds squawk')

bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()
