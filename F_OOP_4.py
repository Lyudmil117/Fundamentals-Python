class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        this_list = []
        if species == "mammal":
            this_list = self.mammals
            species = "Mammals"
        elif species == "fish":
            this_list = self.fishes
            species = "Fishes"
        elif species == "bird":
            this_list = self.birds
            species = "Birds"

        return f"{species} in {self.zoo_name}: {', '.join(this_list)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
number_of_animals = int(input())
animal = Zoo(zoo_name)

for a in range(number_of_animals):
    this_species, this_name = input().split()
    animal.add_animal(this_species, this_name)

what_specie = input()

print(animal.get_info(what_specie))