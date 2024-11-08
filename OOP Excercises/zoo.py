"""Zoo crazy."""


class Animal:
    """Animal class."""

    def __init__(self, name: str, species: str, age: int):
        """
        Class constructor.

        Each animal has a name, a species, and an age.

        :param name: Animal name.
        :param specie: Animal species.
        :param age: Animal age.
        """
        self.name = name
        self.specie = species
        self.age = age

    def __repr__(self):
        """Return a representation of the animal."""
        return f"Animal(name={self.name}, specie={self.specie}, age={self.age})"


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and a max number of animals it can hold.
        There is also an overview of all animals present in the zoo.

        :param name: Zoo name.
        :param max_number_of_animals: Maximum number of animals the zoo can hold.
        """
        self.name = name
        self.max_number = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if an animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed the zoo's max number of animals.
        2. The same Animal object is not already present in the zoo.
        3. An animal with the same name and species is not already present in the zoo.

        :param animal: Animal to check.
        :return: Boolean indicating whether the animal can be added to the zoo.
        """
        if len(self.animals) >= self.max_number:
            return False

        for existing_animal in self.animals:
            if existing_animal is animal or (existing_animal.name == animal.name and existing_animal.specie == animal.specie):
                return False

        return True

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal):
            self.animals.append(animal)

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        for existing_animal in self.animals:
            if existing_animal is animal or (existing_animal.name == animal.name and existing_animal.specie == animal.specie):
                return True
        return False

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        for i in self.animals:
            if i.name == animal.name and i.specie == animal.specie:
                self.animals.remove(i)
                break

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.animals, key=lambda an: an.age)

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        return sorted(self.animals, key=lambda an: an.name)


zoo = Zoo("Aafrika", 12)
znimal = Animal("Ahv", "TOnt", 112)
znimal2 = Animal("Ah2v", "T567nt", 42)
znimal3 = Animal("Ahv3", "T769nt", 32)
znimal4 = Animal("Ah4v", "T567nt", 69)
zoo.add_animal(znimal)
zoo.add_animal(znimal2)
zoo.add_animal(znimal3)
zoo.add_animal(znimal4)
print(zoo.get_animals_by_age())
print(zoo.get_animals_sorted_alphabetically())