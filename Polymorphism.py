# classes cat and dog
class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()


my_cat = Cat()
my_dog = Dog()


animal_sound(my_cat)
animal_sound(my_dog)
