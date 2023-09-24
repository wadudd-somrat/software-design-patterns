We define an abstract Document class (or interface) that represents documents with three components: header, body, and footer. Each of these components is created using abstract methods.

We create concrete document classes, Resume and Report, which inherit from the Document class and provide concrete implementations of the create_header, create_body, and create_footer methods.

We create a DocumentCreator class that has an abstract create_document method. This class allows us to define different creators for different types of documents.

We create concrete document creator classes, ResumeCreator and ReportCreator, which inherit from DocumentCreator and provide their own implementation of the create_document method to specify which type of document to create.

In the client code, we create instances of the concrete document creators (ResumeCreator and ReportCreator) and use them to create documents. The client code can work with documents without needing to know their specific classes.