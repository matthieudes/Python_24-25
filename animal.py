

class Animal():
    """A simple class to represent an animal"""
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return(f"Hello, my name is {self.name}")
    
class Dog(Animal):
    """Represent a dog, a type of animal"""
    def say_hello(self):
        return(f"Woof, my name is {self.name}")

class Cat(Animal):
    """Represent a cat, a type of animal"""
    def say_hello(self):
        return(f"Meow, my name is {self.name}")

animal = Animal("huglo")
dog = Dog("hugro")
cat = Cat("hugo")
print(animal.say_hello())
print(dog.say_hello())
print(cat.say_hello())
