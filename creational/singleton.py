
class Singleton:
    """
    Singleton is a design pattern that ensures that a class can only have one instance, and provides a global point of access to that instance
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# singleton can be implemented like a decorator
def singleton_decorator(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton_decorator
class C:
    def __init__(self, name):
        self.name = name
