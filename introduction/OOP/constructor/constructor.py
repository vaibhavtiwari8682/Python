'''

constructor represented as 
__init__()
'''

class Car:
    def __init__(self,brand,color):
     self.brand   = brand
     self.color = color

car1 = Car('tesla' , 'red') #values automatically set
print(car1.brand, car1.color)


"""
syntax of constructor:
class ClassName:
def __init__(self,parameters1, parameters2):
  self.property1 = parameter1
  self.property = paramter2

  __init__() constructor

  self.property:

"""

