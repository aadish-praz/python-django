

''' Abstract Method , Abstract Class '''

''' if abstract method is used it must be used in the child class'''

from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    def eats(self):
        print('Animal is eating')
        
class Dog(Animal):
    
    def sound(self):
        print('Dog is barking')
        
class Cat(Animal):
    
    def sound(self):
        print('Cat meows')
        
d=Dog()
d.sound()
d.eats()

c=Cat()
c.sound()
c.eats()