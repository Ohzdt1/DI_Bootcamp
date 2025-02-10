#🌟 Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Grumpy' , 2)
cat2 = Cat('Fluffy', 3)
cat3 = Cat('Mittens', 1)

def get_age(cat):
    return cat.age

def eldest_cat(*cats):
    return max(cats, key=get_age)

oldest = eldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, who is {oldest.age} years old.")

###found this but did not quite understand teh lambda 

        # def eldest_cat(*cats):
        #     return max(cats, key=lambda cat: cat.age)

        # oldest = eldest_cat(cat1, cat2, cat3)
        # print(f"The oldest cat is {oldest.name}, who is {oldest.age} years old.")


class Dog:
    dogs = []
    def __init__(self, name, height):
        self.name = name 
        self.height = height 
        print(f"This dog's name is", self.name, "and he is", self.height,"cm tall")
        Dog.dogs.append(self)
        
    def bark(self):
        print(f"{self.name} barks WOOF!")

    def jump(self):
        cm = self.height * 2
        print(f"{self.name} 'Jumps' {cm}cm high!") 

davids_dog = Dog("Rex", 50)  

davids_dog
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

sarahs_dog
sarahs_dog.bark()
sarahs_dog.jump()

def find_biggest_dog(dogs):
    biggest_dog = dogs[0]
    for dog in dogs:
        if dog.height > biggest_dog.height:
            biggest_dog = dog
    return biggest_dog

biggest = find_biggest_dog(Dog.dogs)
print(f"The biggest dog is {biggest.name} with a height of {biggest.height} cm.")


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])


stairway.sing_me_a_song()


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name 
        self.animals = []
        
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo.")
    
    def get_animals(self):
        print(f"Animals in {self.zoo_name}:")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)
        
        return grouped_animals
    
    def get_groups(self):
        grouped = self.sort_animals()
        for letter, animals in grouped.items():
            print(f"{letter}: {', '.join(animals)}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Lion")

ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()
