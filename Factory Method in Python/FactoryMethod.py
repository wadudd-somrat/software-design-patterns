from abc import ABC, abstractmethod

# Step 1: Define an abstract document class (or interface)
class Document(ABC):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_footer(self):
        pass

# Step 2: Create concrete document classes
class Resume(Document):
    def create_header(self):
        return "Resume Header"

    def create_body(self):
        return "Resume Body"

    def create_footer(self):
        return "Resume Footer"

class Report(Document):
    def create_header(self):
        return "Report Header"

    def create_body(self):
        return "Report Body"

    def create_footer(self):
        return "Report Footer"

# Step 3: Create a document creator class
class DocumentCreator:
    @abstractmethod
    def create_document(self):
        pass

    def get_document(self):
        return self.create_document()

# Step 4: Create concrete document creator classes
class ResumeCreator(DocumentCreator):
    def create_document(self):
        return Resume()

class ReportCreator(DocumentCreator):
    def create_document(self):
        return Report()

# Client code
def client_code(creator):
    document = creator.get_document()
    print(f"Header: {document.create_header()}")
    print(f"Body: {document.create_body()}")
    print(f"Footer: {document.create_footer()}")

if __name__ == "__main__":
    print("Creating a Resume:")
    client_code(ResumeCreator())

    print("\nCreating a Report:")
    client_code(ReportCreator())
