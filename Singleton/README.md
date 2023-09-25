1. We define a decorator function singleton that takes a class cls as its argument. The singleton decorator will be used to decorate the class we want to make a singleton.

2. Within the singleton decorator, we define a nested function get_instance. This function checks if an instance of the class cls exists in the instances dictionary. If not, it creates a new instance and stores it in the dictionary. If an instance already exists, it returns the existing instance.

3. Finally, we return the get_instance function as the result of the singleton decorator.

4. In the usage section, we decorate the SingletonClass with the @singleton decorator. This ensures that only one instance of SingletonClass is created, no matter how many times we instantiate it.