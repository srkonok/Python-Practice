class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("Walk !")


class Fish(Animal):
    def swim(self):
        print("Swim ")


m = Mammal()
m.eat()

print(m.age)
print("Is m instance of Animal ? ", isinstance(m, Animal))
o = object()

print("Is m instance of object ? ", isinstance(m, object))
print("Is Mammal Subclass of Animal? ", issubclass(Mammal, Animal))
