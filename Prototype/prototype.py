import copy

# Step 1: Create a prototype class
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Step 2: Create concrete prototype objects
class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ConcretePrototype1 with value: {self.value}"

class ConcretePrototype2(Prototype):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"ConcretePrototype2 with text: {self.text}"

# Step 3: Client code
if __name__ == "__main__":
    prototype1 = ConcretePrototype1(100)
    clone1 = prototype1.clone()
    print(clone1)  # Output: ConcretePrototype1 with value: 100

    prototype2 = ConcretePrototype2("Hello, Prototype!")
    clone2 = prototype2.clone()
    print(clone2) 