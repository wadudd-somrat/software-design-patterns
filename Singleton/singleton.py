def singleton(cls):
    instances = {} 

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# Usage
@singleton
class SingletonClass:
    def __init__(self, value):
        self.value = value

# Create instances
singleton_instance1 = SingletonClass(1)
singleton_instance2 = SingletonClass(2)

# Check if they are the same instance
print(singleton_instance1 is singleton_instance2)  