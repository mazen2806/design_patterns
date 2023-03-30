import unittest
from creational.singleton import Singleton, C



class TestSingletonClass(unittest.TestCase):
    def test_singleton(self):
        s1 = Singleton()
        s2 = Singleton()

        self.assertIs(s1, s2)

    def test_singleton_decorator(self):
        c1 = C(1)
        c2 = C(2)

        self.assertIs(c1, c2)
        self.assertEqual(c1.name, c2.name)
