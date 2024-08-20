# A Singleton can also be implemented using a decorator
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Singleton:
    def __init__(self, value):
        self.value = value

# Example Usage:
singleton1 = Singleton("First Instance")
singleton2 = Singleton("Second Instance")

print(singleton1.value)  # Output: First Instance
print(singleton2.value)  # Output: First Instance

print(singleton1 is singleton2)  # Output: True














# Another advanced approach is using a metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Example Usage:
singleton1 = Singleton("First Instance")
singleton2 = Singleton("Second Instance")

print(singleton1.value)  # Output: First Instance
print(singleton2.value)  # Output: First Instance

print(singleton1 is singleton2)  # Output: True
