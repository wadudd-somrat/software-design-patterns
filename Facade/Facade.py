# Subsystem 1
class SubsystemA:
    def operation_a1(self):
        print("Subsystem A: Operation A1")

    def operation_a2(self):
        print("Subsystem A: Operation A2")

# Subsystem 2
class SubsystemB:
    def operation_b1(self):
        print("Subsystem B: Operation B1")

    def operation_b2(self):
        print("Subsystem B: Operation B2")

# Subsystem 3
class SubsystemC:
    def operation_c1(self):
        print("Subsystem C: Operation C1")

# Facade
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def operation_1(self):
        print("Facade: Operation 1")
        self.subsystem_a.operation_a1()
        self.subsystem_b.operation_b1()
        self.subsystem_c.operation_c1()

    def operation_2(self):
        print("Facade: Operation 2")
        self.subsystem_b.operation_b2()
        self.subsystem_c.operation_c1()

# Client code
if __name__ == "__main__":
    facade = Facade()

    # Using the Facade to perform complex operations
    facade.operation_1()
    facade.operation_2()