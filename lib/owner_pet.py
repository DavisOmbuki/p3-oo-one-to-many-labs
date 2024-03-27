class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.validate_pet_type(pet_type)
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_to_all_pets()

    def validate_pet_type(self, pet_type):
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are: {', '.join(self.PET_TYPES)}")

    def add_to_all_pets(self):
        self.__class__.all_pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all_pets if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets

# Example usage:
try:
    pet1 = Pet("Buddy", "dog")
    pet2 = Pet("Whiskers", "cat")
    pet3 = Pet("Spike", "reptile")

    owner = Owner("John")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)

    sorted_pets = owner.get_sorted_pets()

    print("Owner's pets:")
    for pet in sorted_pets:
        print(f"{pet.name} ({pet.pet_type})")

except Exception as e:
    print(f"Exception: {str(e)}")
