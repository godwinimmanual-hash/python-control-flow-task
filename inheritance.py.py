# inheritance_demo.py

class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof Woof!")


dog = Dog()

dog.sound()   # Inherited method
dog.bark()    # Child class method