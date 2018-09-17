class Dog(object):

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
    # Instance method
    def description(self):
        return ("{} is {} years old" .format(self.name, self.age))
    
    # Instance method
    def speak(self, sound):
        return ("{} says: {}" .format(self.name, sound))

    # Instance method
    def eat(self):
        self.is_hungry = False

     # instance method
    def walk(self):
        return ("{} is walking!" .format(self.name))   
    
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return ("{}'s speed is {} km/hr". format(self.name, speed))

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return ("{}'s speed is {} km/hr". format(self.name, speed))


'''
# Child classes inherit attributes and
# behaviors from the parent class
jim = RussellTerrier("Jim", 5)
print (jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run(20))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
william = Dog("William", 5)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{} is a {}." .format(philo.name, philo.species))

# Calling an instance method
print(philo.description())
#The oldest dog
def get_biggest_number(*args):
    return max(args)

#output
print("the oldest dog is {} years old" .format(get_biggest_number(philo.age, mikey.age, william.age)))
'''