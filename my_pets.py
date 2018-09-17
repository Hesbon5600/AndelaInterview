from TrialClass import Dog, RussellTerrier, Bulldog

class Pet(object):
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs

    # instance method
    def walk(self):
        return ("{} is walking!" .format(dog.name))
# Create instances of dogs
my_dogs = [
    Bulldog("Tim", 7),
    RussellTerrier("Feltcher", 3),
    Dog("Terry", 3)
]
# Instantiate the Pets class
my_pets = Pet(my_dogs)

# Output
print ("I have {} dogs" .format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print ("{} is {}." .format(dog.name, dog.age))

print ("And they're all {}s of course" .format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
for dog in my_pets.dogs:
    dog.walk()
    print(dog.walk())
