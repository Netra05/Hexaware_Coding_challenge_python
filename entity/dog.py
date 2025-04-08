# entity/dog.py

from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed, dog_breed):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed

    def get_dog_breed(self):
        return self.dog_breed

    def set_dog_breed(self, dog_breed):
        self.dog_breed = dog_breed

    def __str__(self):
        return super().__str__() + f", Dog Breed: {self.dog_breed}"
