#inheritance 
class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WOOF!")

dingo = Dog("Dingo")

print(dingo.name)
dingo.bark()


class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an {self.type}, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")


class Giraffe(Animal):
    def eat_leaf(self):
        print("I eat leaf that is high in the tree.")

rex= Dog("dog", 4, "woof")
print('This animal is a:', rex.type)
print('This dog has', rex.number_legs , ' legs')
print('This dog makes the sound', rex.sound)
rex.make_sound()

joshua = Giraffe("Giraffe", 4, "MERAWWERERE")

joshua.make_sound()
joshua.eat_leaf()


