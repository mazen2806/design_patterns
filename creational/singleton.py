
class Singleton:
    """
    Singleton is a design pattern that allows  to create just one instance of a class
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
