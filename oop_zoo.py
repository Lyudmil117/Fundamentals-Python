class Zoo:
    __animals = 0

    def __int__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, spec, name): #spec = species
        if spec == "mammal":
            self.mammals.append(name)
        elif spec == "fish":
            self.fishes.append(name)
        elif spec == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, spec):
        result = ''
        if spec == 'mammal':
            result += f"Mammal in {self.name}: {', '.join(self.mammals)}"
        elif spec == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif spec == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f'\n Total animals: {Zoo.__animals}'

        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = inet(input())

for i in range(number_of_lines):
    info = input().split(' ')
    species = info[0]
    type_of_animal = info[1]
    zoo.add_animal(species, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))

