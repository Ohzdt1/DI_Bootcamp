class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count
    
    def get_info(self):
        info = f"{self.name}'s farm\n"
        
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        
        info += "\n    E-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        
        plural_animal_types = []
        for animal in animal_types:
            if animal == "sheep":
                plural_animal_types.append(animal)  
            else:
                plural_animal_types.append(animal + "s")
        
        return f"{self.name}'s farm has {', '.join(plural_animal_types)}."






macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
