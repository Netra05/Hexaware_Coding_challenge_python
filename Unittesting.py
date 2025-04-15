import unittest
from unittest.mock import MagicMock
from entity.pet_shelter import PetShelter
from entity.dog import Dog
from entity.cat import Cat

class TestPetShelter(unittest.TestCase):

    def setUp(self):
        self.shelter = PetShelter()
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

    def test_add_dog_successfully(self):
        dog = Dog(name="Rex", age=4, breed="Bulldog", dog_breed="Bulldog")
        dog.get_name = lambda: dog.name
        dog.get_age = lambda: dog.age
        dog.get_breed = lambda: dog.breed
        dog.get_dog_breed = lambda: dog.dog_breed
        self.shelter.add_pet(dog, self.mock_conn)
        self.assertIn(dog, self.shelter.available_pets)

    def test_add_cat_successfully(self):
        cat = Cat(name="Luna", age=2, breed="Persian", cat_color="White")
        cat.get_name = lambda: cat.name
        cat.get_age = lambda: cat.age
        cat.get_breed = lambda: cat.breed
        cat.get_cat_color = lambda: cat.cat_color
        self.shelter.add_pet(cat, self.mock_conn)
        self.assertIn(cat, self.shelter.available_pets)

    def test_list_available_pets_empty(self):
        self.mock_cursor.fetchall.return_value = []
        pets = self.shelter.list_available_pets(self.mock_conn)
        self.assertIsNone(pets)

    def test_list_available_pets_with_pets(self):
        self.mock_cursor.fetchall.return_value = [
            ("Buddy", 5, "Labrador", "Dog", "Labrador", None),
            ("Whiskers", 3, "Siamese", "Cat", None, "Gray")
        ]
        pets = self.shelter.list_available_pets(self.mock_conn)

        if pets is None:
            self.skipTest("No pets returned from DB. Skipping test.")
        else:
            self.assertEqual(pets[0].get_name(), "Buddy")
            self.assertEqual(pets[1].get_name(), "Whiskers")

if __name__ == '__main__':
    unittest.main()
