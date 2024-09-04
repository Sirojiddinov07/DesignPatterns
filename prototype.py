import copy


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"

    def clone(self):
        # Use the copy module to clone the object
        return copy.deepcopy(self)


# Create an instance of Person
original_person = Person("John Doe", 30, "123 Elm Street")
print("Original:", original_person)

# Clone the original person
cloned_person = original_person.clone()

# Change some properties in the cloned object
cloned_person.name = "Jane Doe"
cloned_person.address = "456 Oak Avenue"

# Display both objects
print("Cloned:", cloned_person)
print("Original after cloning:", original_person)
