
# Create a program that includes animals 
# or vehicles with the same action (like move()). 
# However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while 
# Plane.move() prints "Flying" ✈️).

# base class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
# subclass for Dog
class Dog(Animal):
    def move(self):
        print("Running ")

# subclass for Cat
class Cat(Animal):
    def move(self):
        print("Walking ")

# subclass for Fish
class Fish(Animal):
    def move(self):
        print("Swimming ")

# list of animals
animals = [Dog(), Cat(), Fish()]
# iterate through the list and call move() for each animal
for animal in animals:
    animal.move()






