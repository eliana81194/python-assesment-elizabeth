# Task 6: Object-Oriented Python
# File: task6_oop.py


# ---------------------------------------------------------
# a. Class Animal with class variable species and __init__ (4 marks)
# d. Class variable counter tracking total instances created (4 marks)
# ---------------------------------------------------------
class Animal:
    species = "Generic Animal"  # class variable, shared by all instances
    counter = 0                 # class variable, tracks number of instances created

    def __init__(self, name, sound, age=1):
        self.name = name
        self.sound = sound
        self.__age = age  # private attribute (see part f - encapsulation)

        # Every time a new Animal is created, increase the shared counter
        Animal.counter += 1

    # -----------------------------------------------------
    # b. speak() method - prints the animal's name and sound (4 marks)
    # -----------------------------------------------------
    def speak(self):
        print(f"{self.name} says {self.sound}")

    # -----------------------------------------------------
    # f. Encapsulation - getter/setter for private __age (5 marks)
    # -----------------------------------------------------
    def get_age(self):
        """Getter method to safely access the private __age attribute."""
        return self.__age

    def set_age(self, age):
        """Setter method to safely update the private __age attribute."""
        if age > 0:
            self.__age = age
        else:
            print("Invalid age: age must be a positive number.")


# ---------------------------------------------------------
# e. Inheritance - Dog subclass extends Animal, overrides speak() (5 marks)
# ---------------------------------------------------------
class Dog(Animal):
    species = "Canine"  # overrides the class variable for Dog instances

    def __init__(self, name, age=1):
        # Dogs always bark, so we pass "Bark" as the sound automatically
        super().__init__(name, "Bark", age)

    def speak(self):
        # Overridden version of speak() with dog-specific behaviour
        print(f"{self.name} the dog barks loudly: {self.sound}!")


# ---------------------------------------------------------
# c. Create at least two objects and call speak() on each (3 marks)
# ---------------------------------------------------------
print("c. Creating Objects and Calling speak()")

animal1 = Animal("Cat", "Meow", 3)
animal2 = Animal("Cow", "Moo", 5)

animal1.speak()
animal2.speak()
print()

# ---------------------------------------------------------
# d. Demonstrate the instance counter
# ---------------------------------------------------------
print("d. Instance Counter")
print("Number of Animal instances created so far:", Animal.counter)
print()

# ---------------------------------------------------------
# e. Demonstrate inheritance with Dog subclass
# ---------------------------------------------------------
print("e. Inheritance - Dog Subclass")

dog1 = Dog("Rex", 2)
dog1.speak()  # uses the overridden speak() method
print("Dog species (class variable):", dog1.species)
print("Number of Animal instances created now (Dog counts too):", Animal.counter)
print()

# ---------------------------------------------------------
# f. Demonstrate encapsulation via getter/setter
# ---------------------------------------------------------
print("f. Encapsulation - Getter and Setter for __age")

print("Current age of animal1 (via getter):", animal1.get_age())

animal1.set_age(4)
print("Updated age of animal1 (via setter):", animal1.get_age())

animal1.set_age(-10)  # invalid age, setter should reject this
print("Age after attempting invalid update:", animal1.get_age())

# Direct access to the private attribute from outside the class would fail:
# print(animal1.__age)  # This would raise an AttributeError
