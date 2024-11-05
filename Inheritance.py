# parent class
class Animal:
    def eat(self):
        print("The animal is eating.")
    
    def sleep(self):
        print("The animal is sleeping.")

# child class
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# instance for dog
my_dog = Dog()

# methods that are inherited 
my_dog.eat() 
my_dog.sleep()

# Use child class method
my_dog.bark()     
