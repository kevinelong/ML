class Animal:
    def __init__(self, kind, noise):
        self.kind = kind  # a variable inside a class is called a property, but in python its an attribute.
        self.noise = noise

    def speak(self):  # Function inside of a class is called a method
        print(self.noise)


a = Animal("Wolf", "Howl!!!")
a.speak()


class Pet(Animal):
    def __init__(self, name, kind, noise):
        self.name = name
        super().__init__(kind, noise)

    def speak(self):  # Override the parent/ base class
        print(f"My name is {self.name}, I am a {self.kind} and I go '{self.noise}'.")


class Cat(Pet):  # extends - "is_a kind of" - example of inheritance
    def __init__(self, name):
        super().__init__(name, "Cat", "Meow")  # super is the parent class


c = Cat("Finnley")
c.speak()
