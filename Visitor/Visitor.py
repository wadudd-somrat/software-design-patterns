from abc import ABC, abstractmethod

# Step 1: Define the Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_file(self, file):
        pass

    @abstractmethod
    def visit_directory(self, directory):
        pass

# Step 2: Create concrete Visitor classes
class ListVisitor(Visitor):
    def visit_file(self, file):
        print(f"File: {file.name}")

    def visit_directory(self, directory):
        print(f"Directory: {directory.name}")

# Step 3: Define the Element interface
class FileSystemElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Step 4: Create concrete Element classes
class File(FileSystemElement):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_file(self)

class Directory(FileSystemElement):
    def __init__(self, name):
        self.name = name
        self.children = []

    def accept(self, visitor):
        visitor.visit_directory(self)

    def add_child(self, child):
        self.children.append(child)

# Step 5: Client code
if __name__ == "__main__":
    root = Directory("Root")
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    subdirectory = Directory("Subdirectory")
    file3 = File("file3.txt")

    root.add_child(file1)
    root.add_child(file2)
    root.add_child(subdirectory)
    subdirectory.add_child(file3)

    list_visitor = ListVisitor()
    
    # Visiting the file system structure
    root.accept(list_visitor)