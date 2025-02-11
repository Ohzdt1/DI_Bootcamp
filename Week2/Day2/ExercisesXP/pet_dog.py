import random

from ExercisesXP import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *dog_names):
        all_dogs = ", ".join([dog.name for dog in dog_names])
        print(f"{self.name}, {all_dogs} all play together!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll!",
                f"{self.name} stands on his back legs!",
                f"{self.name} shakes your hand!",
                f"{self.name} plays dead!"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")


