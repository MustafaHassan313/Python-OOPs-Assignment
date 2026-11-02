class Pet:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal

    def get_info(self):
        return f"{self.name} {self.animal}."

my_pet = Pet("Ola", "Dog")
print(my_pet.get_info())


# FOUR PILLARS OF OOPS
# 1. Encapsulation :It means keeping data and functions together inside one class 
# 2. Abstraction :It means showing only important things and hiding extra details 
# 3. Inheritance :It means one class can use the properties of another class
# 4. Polymorphism : It means the same method can work in different ways for different objects