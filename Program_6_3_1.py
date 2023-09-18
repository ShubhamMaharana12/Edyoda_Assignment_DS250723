# Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color.
# You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.


# Program:-

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_skill(self):
        print(f"{self.name} has a hunting skill level of {self.hunting_skill}.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def show_strength(self):
        print(f"{self.name} has a strength level of {self.strength}.")


dog1 = Dog("Zoro", 3, "Brown")
dog1.description()
dog1.get_info()

jack_russell = JackRussellTerrier("Matt", 2, "White", 8)
jack_russell.description()
jack_russell.get_info()
jack_russell.special_skill()

bulldog = Bulldog("Rocky", 4, "Fawn", 10)
bulldog.description()
bulldog.get_info()
bulldog.show_strength()