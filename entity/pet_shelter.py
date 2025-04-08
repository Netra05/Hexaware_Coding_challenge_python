# entity/pet_shelter.py

from exception.null_ref_exception import NullReferenceException

class PetShelter:
    def __init__(self):
        self.available_pets = []

    def add_pet(self, pet, conn):
        try:
            cursor = conn.cursor()
            pet_type = "Dog" if pet.__class__.__name__ == "Dog" else "Cat"

            # Debug print to ensure correct values
            print(f"Adding {pet_type}: Name={pet.get_name()}, Age={pet.get_age()}, Breed={pet.get_breed()}")

            cursor.execute("""
                INSERT INTO pets (name, age, breed, type, dog_breed, cat_color)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                pet.get_name(),
                pet.get_age(),
                pet.get_breed(),
                pet_type,
                pet.get_dog_breed() if pet_type == "Dog" else None,
                pet.get_cat_color() if pet_type == "Cat" else None
            ))

            conn.commit()
            print("New pet registered at the shelter.")

            # Now add to in-memory list only if DB insert succeeded
            self.available_pets.append(pet)

        except Exception as e:
            print("Error inserting into DB:", e)

    def list_available_pets(self):
        if not self.available_pets:
            raise NullReferenceException("There are currently no pets available.")
        for pet in self.available_pets:
            print(pet)
