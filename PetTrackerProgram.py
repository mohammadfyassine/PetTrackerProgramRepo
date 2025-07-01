class Pet:
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

def get_status(self):
        status = {
            True: "Already adopted",
            False: "Available for adoption"
        }
        return status[self.adopted]

def display_info(self):
    status_text = self.get_status()
    return f"{self.name} is a {self.age}-year-old {self.species}. {status_text}."

def mark_adopted(self):
    message = ""
    if not self.adopted:
        self.adopted = True
        message = "Marked as adopted."
    else:
        message = "Already adopted."
    return message

def birthday(self):
    self.age += 1
    return f"{self.name} is now {self.age} years old."

def rename(self, new_name):
    old_name = self.name
    self.name = new_name
    return f"Name changed from {old_name} to {new_name}."

pets = [pet1, pet2, pet3]

def get_non_adopted_pets(pet_list):
    non_adopted = []
    for pet in pet_list:
        if not pet.adopted:
            non_adopted.append(pet)
    return non_adopted

print("\nNon-Adopted Pets:")
for pet in get_non_adopted_pets(pets):
    print(pet.display_info())
